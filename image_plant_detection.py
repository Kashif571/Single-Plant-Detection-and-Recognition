import cv2
import os

#Cascade
cascade = cv2.CascadeClassifier('./golden_pothos_cascade.xml')

#Reading Image
raw_img = cv2.imread(r'./Golden Pothos/3.jpg')

#Percent of original size
scale_percent = 60 
width = int(raw_img.shape[1] * scale_percent / 100)
height = int(raw_img.shape[0] * scale_percent / 100)
dimensions = (width, height)

#Resizing Image
img = cv2.resize(raw_img, dimensions, interpolation = cv2.INTER_AREA)

#Converting to Gray Image
gray_Image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Adding Gaussian Blur
blur=cv2.GaussianBlur(gray_Image,(13,13),cv2.BORDER_DEFAULT)

#Detecting Plant
detection_result, rejectLevels, levelWeights =cascade.detectMultiScale3(blur, scaleFactor=1.0485258, minNeighbors=6, minSize=(30,30),outputRejectLevels = 1)

greaterweightindex = 0
currentweight = levelWeights[0]

#Area with Heighest Confidence
for (weight) in levelWeights:
    if weight > currentweight:
        greaterweightindex = greaterweightindex+1
        currentweight = weight

#Highest Confidence Area 
x = detection_result[greaterweightindex][0]
y = detection_result[greaterweightindex][1]
w = detection_result[greaterweightindex][2]
h = detection_result[greaterweightindex][3]

#Modifying Cofidence
confidence= round(currentweight[0], 2)
finalconfidence= confidence * 100

#Drawing Rectangle
cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), thickness=2)
cv2.rectangle(img,(x,y-35), (x+w, y), (0,0,255), thickness=-1) 

#Adding Text
cv2.putText(img, str(f"Golden Pothos {finalconfidence}%"), (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), thickness=2)

#Displaying Image
cv2.imshow("Detected Plant",img)

#Adding Wait
cv2.waitKey(0)