from ultralytics import YOLO
import cv2
import numpy as np 

def Tracking(model, frame):
    P_image = pts1 =  None
    pts4 = 0
    pts1_updated = False
    pts2 = np.float32([[0, 0], [840, 0],
                        [0, 960], [840, 960]])
    
    while True:
        ret, image = frame.read()
        h,w,c = image.shape
        results = model(image)
        
        for box in results[0].boxes:
            if box.cls == 0:
                x1 = int(box.xyxy[0][0]) - 250
                y1 = int(box.xyxy[0][1]) - 250
                x2 = int(box.xyxy[0][2]) + 250
                y2 = int(box.xyxy[0][3]) + 250
                cv2.rectangle(image,(int(box.xyxy[0][0]),int(box.xyxy[0][1])),(int(box.xyxy[0][2]),int(box.xyxy[0][3])),(255,0,0),(3))
                if 0 <= x1 and x2 <= w and 0 <= y1 and y2 <= h:
                    pts1 = np.float32([[x1, y1], [x2, y1], [x1, y2], [x2, y2]])
                    pts1_updated = True
            else:
                pts1_updated = False
        if pts1 is not None and pts1_updated == False:
            x1 = x1 - 5
            y1 = y1 - 5
            x2 = x2 + 5
            y2 = y2 + 5
            if 0 <= x1 and x2 <= w and 0 <= y1 and y2 <= h:
                pts1 = np.float32([[x1, y1], [x2, y1], [x1, y2], [x2, y2]])      
        if pts1 is not None:
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            P_image = cv2.warpPerspective(image, matrix, (840, 640))
            cv2.imshow("PR_Frame", P_image)

        cv2.imshow("Frame", image)

        if cv2.waitKey(1) == ord("q"):
            break

def main():
    model = YOLO("best.pt")
    frame = cv2.VideoCapture("Data2.mp4")
    Tracking(model, frame)

if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()
