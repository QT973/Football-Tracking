import argparse
from ultralytics import YOLO
import cv2
import numpy as np

def Tracking(model, track_option, zoom_option, input_video, output_video):
   
    cap = cv2.VideoCapture(input_video)
    out = None
    pts1_updated = False
    pts1 = None
    pts2 = np.float32([[0, 0], [840, 0], [0, 960], [840, 960]])
    zoom_factor = int(zoom_option)
    track_number = track_option if track_option != 'ball' else 0
    
    while True:
        ret, image = cap.read()
        if not ret:
            break
        
        h, w, c = image.shape
        results = model(image)
        zoom = int(400/ zoom_factor)
        for box in results[0].boxes:
            if box.cls == track_number:
                x1 = int(box.xyxy[0][0]) - zoom
                y1 = int(box.xyxy[0][1]) - zoom 
                x2 = int(box.xyxy[0][2]) + zoom 
                y2 = int(box.xyxy[0][3]) + zoom 
                
                if 0 <= x1 and x2 <= w and 0 <= y1 and y2 <= h:
                    pts1 = np.float32([[x1, y1], [x2, y1], [x1, y2], [x2, y2]])
                    pts1_updated = True
            else:
                pts1_updated = False 
                
        if pts1 is not None and not pts1_updated:
            x1 -= 5
            y1 -= 5
            x2 += 5
            y2 += 5
            if 0 <= x1 and x2 <= w and 0 <= y1 and y2 <= h:
                pts1 = np.float32([[x1, y1], [x2, y1], [x1, y2], [x2, y2]])             
                
        if pts1 is not None:
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            P_image = cv2.warpPerspective(image, matrix, (840, 640))

            if out is None:
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(output_video, fourcc, 30.0, (840, 640))
                
            out.write(P_image)
            cv2.imshow("PR_Frame", P_image)

        cv2.imshow("Frame", image)

        if cv2.waitKey(1) == ord("q"):
            break
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--object", type=str, default="ball", help="Object to track, e.g. 'ball' or a number.")
    parser.add_argument("-z", "--zoom", type=int, default=1, help="Zoom level.")
    parser.add_argument("-i", "--input", type=str, default="input.mp4", help="Input video file path.")
    parser.add_argument("-u", "--output", type=str, default="output.mp4", help="Output video file path.")
    parser.add_argument("-w", "--weights", type=str, default="best.pt", help="YOLO model weights path.")
    
    args = parser.parse_args()

    model = YOLO(args.weights)
    Tracking(model, args.object, args.zoom, args.input, args.output)

if __name__ == "__main__":
    main()

