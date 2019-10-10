#!/usr/bin/python

########################
# Author: Lixing Dong
# Note: PIL required
# License: GPL
########################

from PIL import Image
from PIL import ImageTk
from PIL.ExifTags import TAGS
import sys, os
import tkinter
#import ImageTk


class ImageCropper:

    def __init__(self):
        self.root = root = tkinter.Tk()
        self.root.bind("<Button-1>", self.__on_mouse_down)
        self.root.bind("<ButtonRelease-1>", self.__on_mouse_release)
        self.root.bind("<B1-Motion>", self.__on_mouse_move)
        self.root.bind("<Key>", self.__on_key_down)
        self.root.bind("<Up>", self.__on_keyUP)
        self.root.bind("<Down>", self.__on_keyDown)
        self.root.bind("<Left>", self.__on_keyLeft)
        self.root.bind("<Right>", self.__on_keyRight)
        self.message = None
        self.rectangle = None
        self.canvas_image = None
        self.canvas_message = None
        self.files = []
        self.ratioList = []
        self.box = [0, 0, 0, 0]
        self.ratio = 0.75
        self.canvas = tkinter.Canvas(self.root, 
                             highlightthickness = 0,
                             bd = 0)

    def get_image_exif(self, image):
        if image is None:
            img_exif = None
        info = image._getexif()
        if info is not None:
            img_exif = {}
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                img_exif[decoded] = value
            return img_exif
        else:
            return None

    def set_file(self, filename):
        '''self.files = []'''
        self.files.append(filename)

    def set_directory(self, directory):
        if not os.path.isdir(directory):
            raise IOError(directory + ' is not a directory')
        files = os.listdir(directory)
        if len(files) == 0:
            print ('No files found in ' + directory)
        self.files = []
        for filename in files:
            if filename[-11:] == 'cropped.jpg':
                print ('Ignore ' + filename)
                continue
            self.files.append(os.path.join(directory, filename))

    def roll_image(self):
        while len(self.files) > 0 and self.set_image(self.files.pop(0)) == False:
            pass


    def rotate(self, image, exif):
        if exif is None:
            return image
        if exif['Orientation'] == 6:
            return image.rotate(-90)

    def set_ratio(self, ratio):
        self.ratio = float(ratio)

    def set_ratioList(self, List):
        self.ratioList = List

    def set_image(self, filename):

        if filename == None:
            return True

        self.filename = filename
        self.outputname = filename[:filename.rfind('.')] + '_cropped'
        try:
            self.img = Image.open(filename)
        except IOError:
            print ('Ignore: ' + filename + ' cannot be opened as an image')
            return False

        exif = self.get_image_exif(self.img)
        #self.img = self.rotate(self.img, exif)
        ratio = float(self.img.size[1]) / self.img.size[0]
        if self.img.size[0] > 1200:
            self.scale = self.img.size[0] / 1200
            self.resized_img = self.img.resize( (self.img.size[0] / self.scale,
                                                   self.img.size[1] / self.scale),
                                                Image.ANTIALIAS )
        if self.img.size[1] > 800:
            self.scale = self.img.size[1] / 800
            self.resized_img = self.img.resize( (self.img.size[0] / self.scale,
                                                    self.img.size[1] / self.scale),
                                                Image.ANTIALIAS )
        if self.img.size[0] <= 1200 and self.img.size[1] <= 800:
            self.resized_img = self.img
            self.scale = 1
        self.photo = ImageTk.PhotoImage(self.resized_img)
        self.canvas.delete(self.canvas_image)
        self.canvas.config(width = self.resized_img.size[0], height = self.resized_img.size[1])
        self.canvas_image = self.canvas.create_image(0, 0, anchor = tkinter.NW, image = self.photo)
        self.canvas.pack(fill = tkinter.BOTH, expand = tkinter.YES)
        self.root.update()

        self.ratio = self.ratioList[0]
        self.ratioList.pop(0)
        return True

    def __on_mouse_down(self, event):
        self.box[0], self.box[1] = event.x, event.y
        self.box[2], self.box[3] = event.x, event.y
        print ("top left coordinates: %s/%s" % (event.x, event.y))
        self.canvas.delete(self.message)

    def __on_mouse_release(self, event):
        print ("bottom_right coordinates: %s/%s" % (self.box[2], self.box[3]))

    def __crop_image(self):
        box = (self.box[0] * self.scale,
               self.box[1] * self.scale,
               self.box[2] * self.scale, 
               self.box[3] * self.scale)
        try:
            cropped = self.img.crop(box)
            if cropped.size[0] == 0 and cropped.size[1] == 0:
                raise SystemError('no size')
            cropped.save(self.outputname + '.jpg', 'jpeg')
            self.message = 'Saved: ' + self.outputname + '.jpg'
            if len(self.files)==0:
                #self.root.destroy()
                self.root.quit()
                #sys.exit(0)
                #return
            #else:
            #    print("Len:" + str(len(self.files)))
        except SystemError as e:
            pass

    def __fix_ratio_point(self, px, py):
        dx = px - self.box[0]
        dy = py - self.box[1]
        if min((dy / self.ratio), dx) == dx:
            dy = int(dx * self.ratio)
        else:
            dx = int(dy / self.ratio)
        return self.box[0] + dx, self.box[1] + dy


    def __on_mouse_move(self, event):
        self.box[2], self.box[3] = self.__fix_ratio_point(event.x, event.y)
        self.__refresh_rectangle()

    def __on_key_down(self, event):
        #print event.char
        if event.char == ' ':
            self.__crop_image()
            self.roll_image()
            self.canvas.delete(self.canvas_message)
            self.canvas_message = self.canvas.create_text(10, 10, anchor = tkinter.NW, text = self.message, fill = 'red')
        elif event.char == 'q':
            self.root.destroy()

    def __on_keyUP(self, event):
        #print 'UP'
        self.box[1] = self.box[1] - 1
        self.box[3] = self.box[3] - 1
        self.__refresh_rectangle()

    def __on_keyDown(self, event):
        self.box[1] = self.box[1] + 1
        self.box[3] = self.box[3] + 1
        self.__refresh_rectangle()
        #print 'Down'

    def __on_keyLeft(self, event):
        #print 'Left'
        self.box[0] = self.box[0] - 1
        self.box[2] = self.box[2] - 1
        self.__refresh_rectangle()

    def __on_keyRight(self, event):
        #print 'Right'
        self.box[0] = self.box[0] + 1
        self.box[2] = self.box[2] + 1
        self.__refresh_rectangle()

    def __refresh_rectangle(self):
        self.canvas.delete(self.rectangle)
        self.rectangle = self.canvas.create_rectangle(self.box[0], self.box[1], self.box[2], self.box[3])

    def run(self):
        self.roll_image()
        print("test")
        self.root.mainloop()


cropper = ImageCropper()

if os.path.isdir(sys.argv[1]):
    cropper.set_directory(sys.argv[1])
elif os.path.isfile(sys.argv[1]):
    cropper.set_file(sys.argv[1])
elif len(sys.argv) > 2:
    if(int(sys.argv[1])==int(4)):
        cropper.set_file(sys.argv[2])#A 0.75
        cropper.set_file(sys.argv[3])#B 0.75
        cropper.set_file(sys.argv[4])#C 0.75
        cropper.set_file(sys.argv[5])#D 0.75
        cropper.set_ratioList([0.75, 0.75, 0.75, 0.75])#ratio 
    elif(int(sys.argv[1])==int(6)):
        cropper.set_file(sys.argv[3])#B ratio 0.5
        cropper.set_file(sys.argv[4])#C ratio 0.5
        cropper.set_file(sys.argv[2])#A ratio 1.0
        cropper.set_file(sys.argv[5])#D ratio 1.0
        cropper.set_file(sys.argv[6])#E ratio 2.0
        cropper.set_file(sys.argv[7])#F ratio 2.0
        cropper.set_ratioList([0.5, 0.5, 1.0, 1.0, 2.0, 2.0])#ratio 

else:
    print (sys.argv[1] + ' is not a file or directory')
    sys.exit()
cropper.run()
