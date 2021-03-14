import cv2
import os

#Cascade
cascade = cv2.CascadeClassifier('./golden_pothos_cascade.xml')

#Reading Image
capture = cv2.VideoCapture(0)

while True:

    success, frame=capture.read()

    #Converting to Gray Image
    gray_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detecting Plant
    detection_result =cascade.detectMultiScale(gray_Image, rejectLevels, levelWeights,  scaleFactor=1.0485258, minNeighbors=6, minSize=(30,30), outputRejectLevels = 'false')
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
capture.release()
cv2.destroyAllWindows()