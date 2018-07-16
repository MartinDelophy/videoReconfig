import cv2
import numpy as np
import threading
from time import ctime,sleep
import base64  
from PIL import Image
from StringIO import StringIO


def readb64(base64_string):
	base64=base64_string
	print base64
	encoded_data = base64.split(',')[1]
	nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	return img

# videoData=[]
# def videoCap():
def readImage(base64data):
	classifier=cv2.CascadeClassifier("E:/opencv2/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml")   
	img = readb64(base64data)
	print img
	h=100
	w=100
	divisor=8
	minSize=(w/divisor,h/divisor)
	faceRects=classifier.detectMultiScale(img,1.2,2,cv2.CASCADE_SCALE_IMAGE,minSize)
	if len(faceRects)>0:
		for faceRect in faceRects:
			x,y,w,h=faceRect
			cv2.circle(img ,(x+w/2,y+h/2),min(w/2,h/2),(255,0,0))
			cv2.circle(img ,(x+w/4,y+h/4),min(w/8,h/8),(255,0,0))
			cv2.circle(img ,(x+3*w/4,y+h/4),min(w/8,h/8),(255,0,0))
			cv2.rectangle(img ,(x+3*w/8,y+3*h/4),(x+5*w/8,y+7*h/8),(255,0,0))
	print cv2
	ls_f=base64.b64encode(img)
	print ls_f
	return ls_f
# def transmitVideo():
# 	res=videoData
# 	print "res"
# 	return res



# threads = []
# t1 = threading.Thread(target=videoCap)
# threads.append(t1)
# t2 = threading.Thread(target=transmitVideo)
# threads.append(t2)

# if __name__ == '__main__':
# 	print threads
# 	for t in threads:
# 		t.setDaemon(True)
# 		t.start()

# 	print "all over %s" %ctime()
