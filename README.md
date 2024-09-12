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
- Link_data: https://www.youtube.com/watch?v=DdLSl73inbU
- You can down in: https://y2meta.app/vi/youtube/DdLSl73inbU with Resolution: 1080p
- You can change the video link to be predicted in main.py
1. Run Code
```bash
python newapp_mp4_generator.py -o [object] -z [zoom] -i [input_video] -u [output_video] -w [weights]
```
### Command-Line Arguments

- `-o`, `--object`: The object to track (e.g., 'ball'). If tracking a specific class, provide the class number.
- `-z`, `--zoom`: Zoom level to apply (default is 1).
- `-i`, `--input`: Path to the input video file.
- `-u`, `--output`: Path where the output video will be saved.
- `-w`, `--weights`: Path to the YOLO model weights file.

Example: 
```bash
python newapp_mp4_generator.py -o ball -z 2 -i input.mp4 -u output.mp4 -w best.pt
```
2. Stop code
```bash
Press the "q" button on the keyboard
```

