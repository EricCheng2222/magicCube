







import os 
import cv2
import sys, os



currentDir = os.getcwd()
testPyDir  = os.path.join(currentDir, 'test.py')
cropPyDir  = os.path.join(currentDir, 'crop.py ')
cardPyDir  = os.path.join(currentDir, 'card.py')
cubePyDir  = os.path.join(currentDir, 'cube.py')
inputDir = os.path.join(currentDir, "input")

imageA = os.path.join(inputDir, "A.jpg ")
imageB = os.path.join(inputDir, "B.jpg ")
imageC = os.path.join(inputDir, "C.jpg ")
imageD = os.path.join(inputDir, "D.jpg ")
imageE = os.path.join(inputDir, "E.jpg ")
imageF = os.path.join(inputDir, "F.jpg ")

welcomeDir = os.path.join(currentDir, 'welcome')
welcomeDir = os.path.join(welcomeDir, 'welcome.jpg')
welcome = cv2.imread(welcomeDir)
welcome = cv2.resize(welcome, (800, 450))
cv2.imshow('Welcome',welcome)
cv2.waitKey(0)
cv2.destroyAllWindows()

num = input("1,Card\n2,Cube\n3,Exit\n\n\n")
num = int(num)

if num==1:
	welcomeDir = os.path.join(currentDir, 'welcome')
	welcomeDir = os.path.join(welcomeDir, 'Card.jpg')
        print(welcomeDir)
	welcome = cv2.imread(welcomeDir)
	welcome = cv2.resize(welcome, (800, 450))
	cv2.imshow('Welcome',welcome)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	print('python ' + cropPyDir + " 4 "  + imageA + imageB + imageC + imageD)
	os.system('python ' + cropPyDir + " 4 "  + imageA + imageB + imageC + imageD)
	print('python ' + cardPyDir)
        os.system('python ' + cardPyDir)
	
        finishDir = os.path.join(currentDir, "welcome", "finish.jpg")
        finish = cv2.imread(finishDir)
        finish = cv2.resize(finish, (800, 450))
        cv2.imshow("Finish", finish)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

elif num==2:
	welcomeDir = os.path.join(currentDir, 'welcome')
	welcomeDir = os.path.join(welcomeDir, 'cube.jpg')
	welcome = cv2.imread(welcomeDir)
	welcome = cv2.resize(welcome, (800, 450))
	cv2.imshow('Welcome',welcome)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	print('python ' + cropPyDir + " 6 "  + imageA + imageB + imageC + imageD + imageE + imageF)
	os.system('python ' + cropPyDir + " 6 "  + imageA + imageB + imageC + imageD + imageE + imageF)
	os.system('python ' + cubePyDir)

        finishDir = os.path.join(currentDir, "welcome", "finish.jpg")
        finish = cv2.imread(finishDir)
        finish = cv2.resize(finish, (800, 450))
        cv2.imshow("Finish", finish)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
	
else:
	pass
