



import cv2
import numpy as np
import os

(baseH, baseW) = (3000, 2000)

#create blank image
blank_image_front = np.zeros((baseH, baseW, 3), np.uint8)
blank_image_back  = np.zeros((baseH, baseW, 3), np.uint8)

currentDir = os.getcwd()
cardDir = os.path.join(currentDir, "input")

r1, g1, b1 = 0, 0, 0 # Original value
r2, g2, b2 = 255, 255, 255 # Value that we want to replace it with

red, green, blue = blank_image_front[:,:,0], blank_image_front[:,:,1], blank_image_front[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
blank_image_front[:,:,:3][mask] = [r2, g2, b2]

red, green, blue = blank_image_back[:,:,0], blank_image_back[:,:,1], blank_image_back[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
blank_image_back[:,:,:3][mask] = [r2, g2, b2]


A_cropped_dir = os.path.join(cardDir, 'A_cropped.jpg')
B_cropped_dir = os.path.join(cardDir, 'B_cropped.jpg')
C_cropped_dir = os.path.join(cardDir, 'C_cropped.jpg')
D_cropped_dir = os.path.join(cardDir, 'D_cropped.jpg')
print(A_cropped_dir)
#scan pictures named A.jpg, B.jpg, C.jpg, D.jpg in current folder

imageA = cv2.imread(A_cropped_dir)
imageB = cv2.imread(B_cropped_dir)
imageC = cv2.imread(C_cropped_dir)
imageD = cv2.imread(D_cropped_dir)


#crop A, B, C, D


#resize A, B, C, D
tmpDir = os.path.join(currentDir, 'tmp')
resize_A_dir = os.path.join(tmpDir, 'Aresize.jpg')
resize_B_dir = os.path.join(tmpDir, 'Bresize.jpg')
resize_C_dir = os.path.join(tmpDir, 'Cresize.jpg')
resize_D_dir = os.path.join(tmpDir, 'Dresize.jpg')


paste = os.path.join(currentDir, "side")
paste1Dir = os.path.join(paste, "paste1.jpg")
paste2Dir = os.path.join(paste, "paste2.jpg")
paste3Dir = os.path.join(paste, "paste3.jpg")
paste4Dir = os.path.join(paste, "paste4.jpg")
paste1 = cv2.imread(paste1Dir)
paste2 = cv2.imread(paste2Dir)
paste3 = cv2.imread(paste3Dir)
paste4 = cv2.imread(paste4Dir)




(standardH, standardW) = (1500, 2000)
imageA = cv2.resize(imageA, (standardW, standardH))
imageB = cv2.resize(imageB, (standardW, standardH), interpolation = cv2.INTER_LINEAR)
imageC = cv2.resize(imageC, (standardW, standardH), interpolation = cv2.INTER_LINEAR)
imageD = cv2.resize(imageD, (standardW, standardH), interpolation = cv2.INTER_LINEAR)
cv2.imwrite(resize_A_dir, imageA)
cv2.imwrite(resize_B_dir, imageB)
cv2.imwrite(resize_C_dir, imageC)
cv2.imwrite(resize_D_dir, imageD)


#split into 16 pieces
for x in range(0, 4):
	for y in range(0, 4):
		im = imageA[int(standardH/4*(x)):int(standardH/4*(x+1)), int(standardW/4*(y)):int(standardW/4*(y+1))]
		num = str(4*y + x + 1)
		name = "A" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 4):
	for y in range(0, 4):
		im = imageB[int(standardH/4*(x)):int(standardH/4*(x+1)), int(standardW/4*(y)):int(standardW/4*(y+1))]
		num = str(4*y + x + 1)
		name = "B" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 4):
	for y in range(0, 4):
		im = imageC[int(standardH/4*(x)):int(standardH/4*(x+1)), int(standardW/4*(y)):int(standardW/4*(y+1))]
		num = str(4*y + x + 1)
		name = "C" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 4):
	for y in range(0, 4):
		im = imageD[int(standardH/4*(x)):int(standardH/4*(x+1)), int(standardW/4*(y)):int(standardW/4*(y+1))]
		num = str(4*y + x + 1)
		name = "D" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)




#hard code image Alignment
(UnitH, UnitW) = (standardH/4, standardW/4)
UnitH = int(UnitH)
UnitW = int(UnitW)

#A1 - A16
im = cv2.imread(resize_A_dir)
blank_image_front[int(UnitH*2):int(UnitH*6), int(UnitW*0):int(UnitW*4)] = im
#D - upper half
im = cv2.imread(resize_D_dir)
blank_image_front[int(UnitH*0):int(UnitH*2), int(UnitW*0):int(UnitW*4)] = im[int(UnitH*0):UnitH*2, UnitW*0:UnitW*4]
#D - lower half
blank_image_front[UnitH*6:UnitH*8, UnitW*0:UnitW*4] = im[UnitH*2:UnitH*4, UnitW*0:UnitW*4]



#save front

shift = int(standardH/2)
blank_image_front[shift:shift+10, int(standardW/4):int(standardW*3/4)] = [0, 0, 255]
blank_image_front[shift+0:shift+standardH, int(standardW/2-5):int(standardW/2+5)] = [0, 0, 255]
blank_image_front[shift+1500-10:shift+1500, int(standardW/4):int(standardW*3/4)] = [0, 0, 255]

frontDir = os.path.join(currentDir, "output")
frontDir = os.path.join(frontDir, 'front.jpg')
cv2.imwrite(frontDir, blank_image_front)




#B back, B1-4, B13-16
im = cv2.imread(resize_B_dir)
blank_image_back[UnitH*2:UnitH*6, UnitW*2:UnitW*3] = im[UnitH*0:UnitH*4, UnitW*0:UnitW*1]
blank_image_back[UnitH*2:UnitH*6, UnitW*1:UnitW*2] = im[UnitH*0:UnitH*4, UnitW*3:UnitW*4]

B5Dir = os.path.join(tmpDir, "B5.jpg")
im = cv2.imread(B5Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*1:UnitH*2, UnitW*2:UnitW*3] = im


B6Dir = os.path.join(tmpDir, "B6.jpg")
im = cv2.imread(B6Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*0:UnitH*1, UnitW*2:UnitW*3] = im


B7Dir = os.path.join(tmpDir, "B7.jpg")
im = cv2.imread(B7Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*7:UnitH*8, UnitW*2:UnitW*3] = im

B8Dir = os.path.join(tmpDir, "B8.jpg")
im = cv2.imread(B8Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*6:UnitH*7, UnitW*2:UnitW*3] = im


B9Dir = os.path.join(tmpDir, "B9.jpg")
im = cv2.imread(B9Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*1:UnitH*2, UnitW*1:UnitW*2] = im


B10Dir = os.path.join(tmpDir, "B10.jpg")
im = cv2.imread(B10Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*0:UnitH*1, UnitW*1:UnitW*2] = im



B11Dir = os.path.join(tmpDir, "B11.jpg")
im = cv2.imread(B11Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*7:UnitH*8, UnitW*1:UnitW*2] = im


B12Dir = os.path.join(tmpDir, "B12.jpg")
im = cv2.imread(B12Dir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_back[UnitH*6:UnitH*7, UnitW*1:UnitW*2] = im


C5Dir = os.path.join(tmpDir, "C5.jpg")
im = cv2.imread(C5Dir)
blank_image_back[UnitH*0:UnitH*1, UnitW*3:UnitW*4] = im


C6Dir = os.path.join(tmpDir, "C6.jpg")
im = cv2.imread(C6Dir)
blank_image_back[UnitH*3:UnitH*4, UnitW*3:UnitW*4] = im


C7Dir = os.path.join(tmpDir, "C7.jpg")
im = cv2.imread(C7Dir)
blank_image_back[UnitH*4:UnitH*5, UnitW*3:UnitW*4] = im


C8Dir = os.path.join(tmpDir, "C8.jpg")
im = cv2.imread(C8Dir)
blank_image_back[UnitH*7:UnitH*8, UnitW*3:UnitW*4] = im


C9Dir = os.path.join(tmpDir, "C9.jpg")
im = cv2.imread(C9Dir)
blank_image_back[UnitH*0:UnitH*1, UnitW*0:UnitW*1] = im


C10Dir = os.path.join(tmpDir, "C10.jpg")
im = cv2.imread(C10Dir)
blank_image_back[UnitH*3:UnitH*4, UnitW*0:UnitW*1] = im


C11Dir = os.path.join(tmpDir, "C11.jpg")
im = cv2.imread(C11Dir)
blank_image_back[UnitH*4:UnitH*5, UnitW*0:UnitW*1] = im


C12Dir = os.path.join(tmpDir, "C12.jpg")
im = cv2.imread(C12Dir)
blank_image_back[UnitH*7:UnitH*8, UnitW*0:UnitW*1] = im

shift = int(standardH/2)
blank_image_back[shift+0:shift+10, int(standardW/4):int(standardW*3/4)] = [0, 0, 255]
blank_image_back[shift+0:shift+standardH, int(standardW/2-5):int(standardW/2+5)] = [0, 0, 255]
blank_image_back[shift+1500-10:shift+1500, int(standardW/4):int(standardW*3/4)] = [0, 0, 255]


blank_image_back[UnitH*1:UnitH*2, UnitW*0:UnitW*1] = paste1
blank_image_back[UnitH*2:UnitH*3, UnitW*0:UnitW*1] = paste1

blank_image_back[UnitH*5:UnitH*6, UnitW*0:UnitW*1] = paste2
blank_image_back[UnitH*6:UnitH*7, UnitW*0:UnitW*1] = paste2

blank_image_back[UnitH*1:UnitH*2, UnitW*3:UnitW*4] = paste3
blank_image_back[UnitH*2:UnitH*3, UnitW*3:UnitW*4] = paste3

blank_image_back[UnitH*5:UnitH*6, UnitW*3:UnitW*4] = paste4
blank_image_back[UnitH*6:UnitH*7, UnitW*3:UnitW*4] = paste4

backDir = os.path.join(currentDir, "output")
backDir = os.path.join(backDir, 'back.jpg')
cv2.imwrite(backDir, blank_image_back)


