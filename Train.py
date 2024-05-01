from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# Train the model with 2 GPUs
model.train(data='./5_FootballTracking/Data_FootballTracking/data.yaml',  epochs=500,device ="1", imgsz=640, batch=20, workers=2)