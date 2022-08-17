import warnings
warnings.filterwarnings('ignore')
import numpy as np
import cv2

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
font=cv2.FONT_HERSHEY_COMPLEX

def preprocessing(img):
    img=img.astype("uint8")
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.equalizeHist(img)
    img = img/255
    return img

window_name = "ROV - IR Feed"
cv2.namedWindow(window_name, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
	sucess, img_original =cap.read()
	img_original = cv2.flip(img_original, 0)
	faces = facedetect.detectMultiScale(img_original, 1.3, 3)

	for x,y,w,h in faces:
		crop_img=img_original[y:y+h,x:x+h]
		img=cv2.resize(crop_img, (32,32))
		img=preprocessing(img)
		img=img.reshape(1, 32, 32, 1)

		cv2.rectangle(img_original,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.rectangle(img_original, (x,y-40),(x+w, y), (0,0,255),-2)
		cv2.putText(img_original, " HUMAN",(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)

	cv2.putText(img_original, "ROGUES VILLAGE IR FEED - NOT RECORDING" , (20,35), font, 0.5, (255,255,255), 2, cv2.LINE_AA)
	img_original = cv2.resize(img_original, (1280,900))
	cv2.imshow(window_name, img_original)
	k=cv2.waitKey(1)
	if k==ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
