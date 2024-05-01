# SETUP
## Install Environment via Anaconda (Recommended)
```bash
conda create -n FootballTracking python=3.9
conda activate FootballTracking 
pip install -r requirements.txt
```
## Train model
1. Your computer must have a built-in NVIDIA GPU
2. Install the Pytorch version that matches the CUDA version at the link: https://pytorch.org/
3. Run
```bash
Train.py
```
## Predict
You can change the video link to be predicted in main.py
```bash
frame = cv2.VideoCapture("Data2.mp4")
```
1. Run Code
```bash
python main.py
```
3. Stop code
```bash
Press the "q" button on the keyboard
```

