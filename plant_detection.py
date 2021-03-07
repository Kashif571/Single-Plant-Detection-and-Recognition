import cv2
import os

#Cascade
cascade = cv2.CascadeClassifier('./golden_pothos_cascade.xml')

#Reading Image
raw_img = cv2.imread(r'./Golden Pothos/11.jpg')

#Percent of original size
scale_percent = 60 
width = int(raw_img.shape[1] * scale_percent / 100)
height = int(raw_img.shape[0] * scale_percent / 100)
dimensions = (width, height)

#Resizing Image
img = cv2.resize(raw_img, dimensions, interpolation = cv2.INTER_AREA)

#Adding Median Blur
blur=cv2.medianBlur(img,9)

#Converting to Gray Image
gray_Image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

#Detecting Plant
detection_result = cascade.detectMultiScale(gray_Image, scaleFactor=1.0485258, minNeighbors=6, minSize=(100,100))
print(detection_result)

for (x,y,w,h) in detection_result:
    
    print(x)
    print(y)
    print(w)
    print(h)

    #Draw Rectangle
    cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), thickness=2)

    #Adding Text
    cv2.putText(img, str("Golden Pothos"), (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)

#Displaying Image
cv2.imshow("Detected Plant",img)

#Adding Wait
cv2.waitKey(0)