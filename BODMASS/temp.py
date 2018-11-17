import cv2

#import numpy as np
#data=cv2.VideoCapture(0)
#while ret:
    #ret,image=data.read()

def main():
    windowName = "Preview"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    #create a frame object
    
    if cap.isOpened():
        ret, frame = cap.read()
        print (ret)     #returns if capture is true
        print(frame)    #prints image representation matrix
        grayoutput = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("image captured",grayoutput)
        #cvtColor( image, gray_image, CV_BGR2GRAY )
        #imwrite("Desktop\image.png", frame);
        cv2.imwrite( "C:/Users/pramesh/PycharmProjects/BODMASS/dataset/pics/samp7.jpg", grayoutput);
        cv2.waitKey(0)
        
        # Create window
        #cv2.namedWindow('HemangaWindow')
        # Show an image in the window
        #cv2.createTrackbar('thrs1', 'HemangaWindow', 10, 500, haha)
        #cv2.imshow('HemangaWindow', grayoutput)
        cv2.waitKey(0)
        # Add a slider
        #cv2.createTrackbar("Heman","hehe",234,100,print("haha")

    cap.release()
    cv2.destroyAllWindows()   
