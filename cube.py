



import cv2
import numpy as np
import os


padding = 100
(baseH, baseW) = (3000 + 2*padding, 4000 + 2*padding)
baseH = int(baseH)
baseW = int(baseW)
#create blank image
blank_image_left   = np.zeros((baseH, baseW, 3), np.uint8)
blank_image_right  = np.zeros((baseH, baseW, 3), np.uint8)

r1, g1, b1 = 0, 0, 0 # Original value
r2, g2, b2 = 255, 255, 255 # Value that we want to replace it with

red, green, blue = blank_image_left[:,:,0], blank_image_left[:,:,1], blank_image_left[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
blank_image_left[:,:,:3][mask] = [r2, g2, b2]

red, green, blue = blank_image_right[:,:,0], blank_image_right[:,:,1], blank_image_right[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
blank_image_right[:,:,:3][mask] = [r2, g2, b2]

currentDir = os.getcwd()
cubeInputDir = os.path.join(currentDir, "input")
horizontalDir = os.path.join(cubeInputDir, "horiRect")
verticalDir   = os.path.join(cubeInputDir, "vertRect")
squareDir     = os.path.join(cubeInputDir, "square")
sideDir       = os.path.join(currentDir, "side")

A_cropped_dir = os.path.join(cubeInputDir,  'A_cropped.jpg')
B_cropped_dir = os.path.join(cubeInputDir,  'B_cropped.jpg')
C_cropped_dir = os.path.join(cubeInputDir,  'C_cropped.jpg')
D_cropped_dir = os.path.join(cubeInputDir,  'D_cropped.jpg')
E_cropped_dir = os.path.join(cubeInputDir,  'E_cropped.jpg')
F_cropped_dir = os.path.join(cubeInputDir,  'F_cropped.jpg')



#scan pictures named A.jpg, B.jpg, C.jpg, D.jpg in current folder
imageA = cv2.imread(A_cropped_dir)
imageB = cv2.imread(B_cropped_dir)
imageC = cv2.imread(C_cropped_dir)
imageD = cv2.imread(D_cropped_dir)
imageE = cv2.imread(E_cropped_dir)
imageF = cv2.imread(F_cropped_dir)



#resize A, B, C, D
tmpDir = os.path.join(currentDir, 'tmp')
resize_A_dir = os.path.join(tmpDir, 'Aresize.jpg')
resize_B_dir = os.path.join(tmpDir, 'Bresize.jpg')
resize_C_dir = os.path.join(tmpDir, 'Cresize.jpg')
resize_D_dir = os.path.join(tmpDir, 'Dresize.jpg')
resize_E_dir = os.path.join(tmpDir, 'Eresize.jpg')
resize_F_dir = os.path.join(tmpDir, 'Fresize.jpg')


print("1")
(unitH, unitW) = (500, 500)
imageA = cv2.resize(imageA, (2*unitW, 2*unitH), interpolation = cv2.INTER_LINEAR)
imageB = cv2.resize(imageB, (4*unitW, 2*unitH), interpolation = cv2.INTER_LINEAR)
imageC = cv2.resize(imageC, (4*unitW, 2*unitH), interpolation = cv2.INTER_LINEAR)
imageD = cv2.resize(imageD, (2*unitW, 2*unitH), interpolation = cv2.INTER_LINEAR)
imageE = cv2.resize(imageE, (2*unitW, 4*unitH), interpolation = cv2.INTER_LINEAR)
imageF = cv2.resize(imageF, (2*unitW, 4*unitH), interpolation = cv2.INTER_LINEAR)


print("2")
cv2.imwrite(resize_A_dir, imageA)
cv2.imwrite(resize_B_dir, imageB)
cv2.imwrite(resize_C_dir, imageC)
cv2.imwrite(resize_D_dir, imageD)
cv2.imwrite(resize_E_dir, imageE)
cv2.imwrite(resize_F_dir, imageF)


#split into 16 pieces
for x in range(0, 2):
	for y in range(0, 2):
		im = imageA[unitH*(x):unitH*(x+1), unitW*(y):unitW*(y+1)]
		num = str(2*y + x + 1)
		name = "A" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 2):
	for y in range(0, 4):
		im = imageB[unitH*(x):unitH*(x+1), unitW*(y):unitW*(y+1)]
		num = str(2*y + x + 1)
		name = "B" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 2):
	for y in range(0, 4):
		im = imageC[unitH*(x):unitH*(x+1), unitW*(y):unitW*(y+1)]
		num = str(2*y + x + 1)
		name = "C" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 2):
	for y in range(0, 2):
		im = imageD[unitH*(x):unitH*(x+1), unitW*(y):unitW*(y+1)]
		num = str(2*y + x + 1)
		name = "D" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 4):
	for y in range(0, 2):
		im = imageE[unitH*(x):unitH*(x+1), unitW*(y):unitW*(y+1)]
		num = str(4*y + x + 1)
		name = "E" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)

for x in range(0, 4):
	for y in range(0, 2):
		im = imageF[unitH*(x):unitH*(x+1), unitW*(y):unitW*(y+1)]
		num = str(4*y + x + 1)
		name = "F" + num + ".jpg"
		dir = os.path.join(tmpDir, name)
		cv2.imwrite(dir, im)




#hard code image Alignment
topDir = os.path.join(sideDir, "sideTop.jpg")
sideTop = cv2.imread(topDir)
botDir = os.path.join(sideDir, "sideBottom.jpg")
sideBot = cv2.imread(botDir)
lftDir = os.path.join(sideDir, "sideLeft.jpg")
sideLeft = cv2.imread(lftDir)
rghtDir = os.path.join(sideDir, "sideRight.jpg")
sideRight = cv2.imread(rghtDir)


blank_image_left[unitH*0:unitH*0 + padding, unitW*7 + padding:unitW*8 + padding] = sideTop
blank_image_left[unitH*1:unitH*1 + padding, unitW*0 + padding:unitW*1 + padding] = sideTop
blank_image_left[unitH*1:unitH*1 + padding, unitW*1 + padding:unitW*2 + padding] = sideTop
blank_image_left[unitH*1:unitH*1 + padding, unitW*2 + padding:unitW*3 + padding] = sideTop
blank_image_left[unitH*1:unitH*1 + padding, unitW*6 + padding:unitW*7 + padding] = sideTop
blank_image_left[unitH*4:unitH*4 + padding, unitW*0 + padding:unitW*1 + padding] = sideTop
blank_image_left[unitH*4:unitH*4 + padding, unitW*1 + padding:unitW*2 + padding] = sideTop
blank_image_left[unitH*4:unitH*4 + padding, unitW*2 + padding:unitW*3 + padding] = sideTop
blank_image_left[unitH*4:unitH*4 + padding, unitW*4 + padding:unitW*5 + padding] = sideTop
blank_image_left[unitH*4:unitH*4 + padding, unitW*6 + padding:unitW*7 + padding] = sideTop
blank_image_left[unitH*4:unitH*4 + padding, unitW*7 + padding:unitW*8 + padding] = sideTop

blank_image_left[unitH*2 + padding:unitH*2 + 2*padding, unitW*0 + padding:unitW*1 + padding] = sideBot
blank_image_left[unitH*2 + padding:unitH*2 + 2*padding, unitW*1 + padding:unitW*2 + padding] = sideBot
blank_image_left[unitH*2 + padding:unitH*2 + 2*padding, unitW*2 + padding:unitW*3 + padding] = sideBot
blank_image_left[unitH*2 + padding:unitH*2 + 2*padding, unitW*5 + padding:unitW*6 + padding] = sideBot
blank_image_left[unitH*2 + padding:unitH*2 + 2*padding, unitW*7 + padding:unitW*8 + padding] = sideBot
blank_image_left[unitH*3 + padding:unitH*3 + 2*padding, unitW*6 + padding:unitW*7 + padding] = sideBot
blank_image_left[unitH*5 + padding:unitH*5 + 2*padding, unitW*0 + padding:unitW*1 + padding] = sideBot
blank_image_left[unitH*5 + padding:unitH*5 + 2*padding, unitW*1 + padding:unitW*2 + padding] = sideBot
blank_image_left[unitH*5 + padding:unitH*5 + 2*padding, unitW*2 + padding:unitW*3 + padding] = sideBot
blank_image_left[unitH*5 + padding:unitH*5 + 2*padding, unitW*4 + padding:unitW*5 + padding] = sideBot
blank_image_left[unitH*5 + padding:unitH*5 + 2*padding, unitW*6 + padding:unitW*7 + padding] = sideBot
blank_image_left[unitH*6 + padding:unitH*6 + 2*padding, unitW*7 + padding:unitW*8 + padding] = sideBot

blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*0 :unitW*0 + padding] = sideLeft
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*0 :unitW*0 + padding] = sideLeft
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*0 :unitW*0 + padding] = sideLeft

blank_image_left[unitH*0 + padding:unitH*1 + padding, unitW*8+ padding :unitW*8 + 2*padding] = sideRight
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*8+ padding :unitW*8 + 2*padding] = sideRight
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*8+ padding :unitW*8 + 2*padding] = sideRight


padding = int(padding)
#A1
imDir = os.path.join(tmpDir, "C4.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*0 + padding:unitH*1 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "A1.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 0, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*0 + padding:unitH*1 + padding, unitW*5 + padding:unitW*6 + padding] = im

imDir = os.path.join(tmpDir, "C2.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 0, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*0 + padding:unitH*1 + padding, unitW*7 + padding:unitW*8 + padding] = im


#A2
imDir = os.path.join(tmpDir, "B4.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 0, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*0 + padding:unitW*1 + padding] = im

imDir = os.path.join(tmpDir, "D2.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*1 + padding:unitW*2 + padding] = im

imDir = os.path.join(tmpDir, "E4.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "E3.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*4 + padding:unitW*5 + padding] = im

imDir = os.path.join(tmpDir, "A2.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 0, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*5 + padding:unitW*6 + padding] = im

imDir = os.path.join(tmpDir, "B2.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 0, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*1 + padding:unitH*2 + padding, unitW*7 + padding:unitW*8 + padding] = im

imDir = os.path.join(tmpDir, "F4.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*2 + padding:unitH*3 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "F3.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*2 + padding:unitH*3 + padding, unitW*6 + padding:unitW*7 + padding] = im


imDir = os.path.join(tmpDir, "F8.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*3 + padding:unitH*4 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "F7.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*3 + padding:unitH*4 + padding, unitW*5 + padding:unitW*6 + padding] = im

imDir = os.path.join(tmpDir, "B6.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*0 + padding:unitW*1 + padding] = im

imDir = os.path.join(tmpDir, "D4.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*1 + padding:unitW*2 + padding] = im

imDir = os.path.join(tmpDir, "E8.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "E7.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*4 + padding:unitW*5 + padding] = im

imDir = os.path.join(tmpDir, "A4.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*5 + padding:unitW*6 + padding] = im

imDir = os.path.join(tmpDir, "A4.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*4 + padding:unitH*5 + padding, unitW*7 + padding:unitW*8 + padding] = im


imDir = os.path.join(tmpDir, "C6.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*5 + padding:unitH*6 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "A3.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*5 + padding:unitH*6 + padding, unitW*5 + padding:unitW*6 + padding] = im

imDir = os.path.join(tmpDir, "C8.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_left[unitH*5 + padding:unitH*6 + padding, unitW*7 + padding:unitW*8 + padding] = im

backDir = os.path.join(currentDir, "output")
backDir = os.path.join(backDir, "left.jpg")
cv2.imwrite(backDir, blank_image_left)










blank_image_right[unitH*1:unitH*1 + padding, unitW*0 + padding:unitW*1 + padding] = sideTop
blank_image_right[unitH*1:unitH*1 + padding, unitW*1 + padding:unitW*2 + padding] = sideTop
blank_image_right[unitH*1:unitH*1 + padding, unitW*3 + padding:unitW*4 + padding] = sideTop
blank_image_right[unitH*1:unitH*1 + padding, unitW*5 + padding:unitW*6 + padding] = sideTop
blank_image_right[unitH*1:unitH*1 + padding, unitW*6 + padding:unitW*7 + padding] = sideTop
blank_image_right[unitH*1:unitH*1 + padding, unitW*7 + padding:unitW*8 + padding] = sideTop
blank_image_right[unitH*4:unitH*4 + padding, unitW*0 + padding:unitW*1 + padding] = sideTop
blank_image_right[unitH*4:unitH*4 + padding, unitW*1 + padding:unitW*2 + padding] = sideTop
blank_image_right[unitH*4:unitH*4 + padding, unitW*3 + padding:unitW*4 + padding] = sideTop
blank_image_right[unitH*4:unitH*4 + padding, unitW*5 + padding:unitW*6 + padding] = sideTop
blank_image_right[unitH*4:unitH*4 + padding, unitW*6 + padding:unitW*7 + padding] = sideTop
blank_image_right[unitH*4:unitH*4 + padding, unitW*7 + padding:unitW*8 + padding] = sideTop

blank_image_right[unitH*2 + padding:unitH*2 + 2*padding, unitW*0 + padding:unitW*1 + padding] = sideBot
blank_image_right[unitH*2 + padding:unitH*2 + 2*padding, unitW*2 + padding:unitW*3 + padding] = sideBot
blank_image_right[unitH*2 + padding:unitH*2 + 2*padding, unitW*3 + padding:unitW*4 + padding] = sideBot
blank_image_right[unitH*2 + padding:unitH*2 + 2*padding, unitW*5 + padding:unitW*6 + padding] = sideBot
blank_image_right[unitH*2 + padding:unitH*2 + 2*padding, unitW*6 + padding:unitW*7 + padding] = sideBot
blank_image_right[unitH*2 + padding:unitH*2 + 2*padding, unitW*7 + padding:unitW*8 + padding] = sideBot
blank_image_right[unitH*5 + padding:unitH*5 + 2*padding, unitW*0 + padding:unitW*1 + padding] = sideBot
blank_image_right[unitH*5 + padding:unitH*5 + 2*padding, unitW*2 + padding:unitW*3 + padding] = sideBot
blank_image_right[unitH*5 + padding:unitH*5 + 2*padding, unitW*3 + padding:unitW*4 + padding] = sideBot
blank_image_right[unitH*5 + padding:unitH*5 + 2*padding, unitW*5 + padding:unitW*6 + padding] = sideBot
blank_image_right[unitH*5 + padding:unitH*5 + 2*padding, unitW*6 + padding:unitW*7 + padding] = sideBot
blank_image_right[unitH*5 + padding:unitH*5 + 2*padding, unitW*7 + padding:unitW*8 + padding] = sideBot

blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*0 :unitW*0 + padding] = sideLeft
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*0 :unitW*0 + padding] = sideLeft

blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*8+ padding :unitW*8 + 2*padding] = sideRight
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*8+ padding :unitW*8 + 2*padding] = sideRight


imDir = os.path.join(tmpDir, "C1.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 0, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*0 + padding:unitH*1 + padding, unitW*2 + padding:unitW*3 + padding] = im

imDir = os.path.join(tmpDir, "C3.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*0 + padding:unitH*1 + padding, unitW*4 + padding:unitW*5 + padding] = im

imDir = os.path.join(tmpDir, "B1.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*0 + padding:unitW*1 + padding] = im

imDir = os.path.join(tmpDir, "A1.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*2 + padding:unitW*3 + padding] = im

imDir = os.path.join(tmpDir, "E2.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "E1.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*4 + padding:unitW*5 + padding] = im

imDir = os.path.join(tmpDir, "D1.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*6 + padding:unitW*7 + padding] = im

imDir = os.path.join(tmpDir, "B3.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*1 + padding:unitH*2 + padding, unitW*7 + padding:unitW*8 + padding] = im

imDir = os.path.join(tmpDir, "F2.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*2 + padding:unitH*3 + padding, unitW*1 + padding:unitW*2 + padding] = im

imDir = os.path.join(tmpDir, "F1.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*2 + padding:unitH*3 + padding, unitW*4 + padding:unitW*5 + padding] = im

imDir = os.path.join(tmpDir, "F6.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*3 + padding:unitH*4 + padding, unitW*2 + padding:unitW*3 + padding] = im

imDir = os.path.join(tmpDir, "F5.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*3 + padding:unitH*4 + padding, unitW*4 + padding:unitW*5 + padding] = im

imDir = os.path.join(tmpDir, "B7.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*0 + padding:unitW*1 + padding] = im

imDir = os.path.join(tmpDir, "A3.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*2 + padding:unitW*3 + padding] = im

imDir = os.path.join(tmpDir, "E6.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*3 + padding:unitW*4 + padding] = im

imDir = os.path.join(tmpDir, "E5.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*4 + padding:unitW*5 + padding] = im

imDir = os.path.join(tmpDir, "D3.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*6 + padding:unitW*7 + padding] = im

imDir = os.path.join(tmpDir, "B5.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*4 + padding:unitH*5 + padding, unitW*7 + padding:unitW*8 + padding] = im

imDir = os.path.join(tmpDir, "C7.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*5 + padding:unitH*6 + padding, unitW*1 + padding:unitW*2 + padding] = im

imDir = os.path.join(tmpDir, "C5.jpg")
im = cv2.imread(imDir)
(h, w) = im.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) #180degree
im = cv2.warpAffine(im, M, (w, h))
blank_image_right[unitH*5 + padding:unitH*6 + padding, unitW*4 + padding:unitW*5 + padding] = im

backDir = os.path.join(currentDir, "output")
backDir = os.path.join(backDir, "right.jpg")
cv2.imwrite(backDir, blank_image_right)
