import cv2 #open cv for image processing
#Creting a video capture opject
cap = cv2.VideoCapture(0) #This is my web camp

#getting the background image
while cap.isOpened():
    ret, background = cap.read() #simply reading from the web camp
    if ret:
        cv2.imshow("image", background)
        if cv2.waitKey(5) == ord('q'):
            #Save the bg imgae
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()