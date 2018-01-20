﻿from random import randint
import cv2
import sys
import os
      
CASCADE="face_cas.xml"
FACE_CASCADE=cv2.CascadeClassifier(CASCADE)

def detect_faces(image_path):

	image=cv2.imread(image_path)
	image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	faces = FACE_CASCADE.detectMultiScale(image_grey,scaleFactor=1.05,minNeighbors=5,minSize=(20,20),flags=0)
	#print faces
	for x,y,w,h in faces:
	    sub_img=image[y-50:y+h+50,x-50:x+w+50]
	    os.chdir("Extracted")
	    cv2.imwrite(str(randint(0,10000))+".jpg",sub_img)
	    os.chdir("../")
	    cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)

	cv2.imshow("Faces Found",image)
	if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
		cv2.destroyAllWindows()

if __name__ == "__main__":
	
	if not "Extracted" in os.listdir("."):
		os.mkdir("Extracted")
    
	if len(sys.argv) < 2:
		print "Usage: python Detect_face.py 'image path'"
		sys.exit()

	detect_faces(sys.argv[1])