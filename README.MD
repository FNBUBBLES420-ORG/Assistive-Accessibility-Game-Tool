<p align="center">
  <img src="https://github.com/FNBUBBLES420-ORG/Assistive-AimGuide/blob/main/banner/Assitive-AimGuide.png" alt="Assistive-AimGuide" width="350">
</p>

<p align="center">
  <img src="https://github.com/FNBUBBLES420-ORG/Assistive-AimGuide/blob/main/banner/fnbubbles420.png" alt="Fnbubbles420 Logo" width="80" align="left">
  <img src="https://github.com/FNBUBBLES420-ORG/Assistive-AimGuide/blob/main/banner/fnbubbles420.png" alt="Fnbubbles420 Logo" width="80" align="right">
  <br><br><br>
  <h1 align="center">FNBubbles420 Org - Assistive Aim-Guide</h1>
</p>


# Assistive Accessibility Game Tool 🎯

Welcome to the Assistive Accessibility Game Tool project! This tool is designed to support individuals with disabilities by helping identify and aim at players within a game window using object detection.

## 🧠 What It Does

- Detects human targets using ONNX models (e.g. YOLOv5/YOLOv8).
- Aims towards detected targets using mouse simulation.
- Uses human-like smooth mouse movements for natural aiming.
- Configurable detection threshold and headshot mode.
- Includes masking and camera region selection features.
- Draws bounding boxes directly on the frame using OpenCV (no separate overlay module).

## 🚀 Getting Started

### 1. Install Python
Use the provided script to install Python 3.11.9:
```bat
python3119.bat
```
This will download and install Python and set it in your system PATH.

### 2. Install Requirements
Make sure you install all required packages by running:
```bat
launcher.bat
```
This will execute `launcher.py`, which installs dependencies from `requirements.txt` and sets up the tool.

### 3. Edit and Save Your Configuration
Once the application is launched via `launcher.bat`, a graphical window will open.

1. Use the interface to open the `config.py` file.
2. Modify your settings (e.g. resolution, input keys, GPU type, etc.).
3. Click **Save** inside the GUI after editing the config so the changes take effect.

You must save the `config.py` before proceeding with running the tool.

### 4. Run the Main Application
After saving your configuration through the GUI, you can use:
```bat
launcher.bat
```
again to relaunch the main application with the updated configuration.

## ✅ Required Python Packages (in `requirements.txt`)
```txt
# torch without CUDA support is for AMD GPUs
torch==2.6.0
torchvision==0.21.0
torchaudio==2.6.0
# Uncomment the following lines if you are using Nvidia GPUs
# torch==2.6.0+cu118
# torchaudio==2.6.0+cu118
# torchvision==0.21.0+cu118
numpy==1.26.4
onnxruntime-gpu==1.16.3
onnxruntime-directml==1.16.3
opencv-python
comtypes
customtkinter
pandas
# uncomment the following line Below if you are using Nvidia GPUs
# cupy-cuda11x
bettercam
psutil
colorama
ultralytics
PyAutoGUI
PyGetWindow
pywin32
pyyaml
tqdm
matplotlib
seaborn
requests
ipython
dxcam
onnx
# uncomment the following line if you are using Nvidia GPUs
# onnxruntime-gpu
onnx-simplifier
dill
serial
pyserial
pyarmor
# DirectML dependencies for Windows AMD GPUs
# torch-directml
# onnxruntime-directml==1.16.3
```

### 🔧 Configuration (`config.py` Example)
```python
from win32con import VK_RBUTTON

# Screen capture settings
screenShotHeight = 320
screenShotWidth = 320

# Mask settings
useMask = True
maskSide = "left"
maskWidth = 140
maskHeight = 240

# Autoaim settings
aaMovementAmp = 1.0
aaQuitKey = "8"
aaActivationKey = VK_RBUTTON
headshot_mode = True

# Confidence threshold
confidence = 0.25

# Serial communication settings
enableSerial = True
fallbackSerialPort = "COM3"
baudRate = 115200

# Display settings
cpsDisplay = True
visuals = True

# Target selection
centerOfScreen = True

# ONNX model settings
onnxProvider = 'CUDAExecutionProvider'
model_path = 'onnx-models/v5_mini_royale.onnx'
device = 'cuda'
fp16 = True
```

## ⚙️ Supported GPU Providers
Use the correct `onnxProvider` in `config.py` depending on your hardware:
- `'CUDAExecutionProvider'` – for NVIDIA (requires CUDA 11.x and cuDNN)
- `'DmlExecutionProvider'` – for AMD GPUs (requires DirectML)
- `'CPUExecutionProvider'` – fallback for general use

## 🧩 System Overview
- Captures game feed using `dxcam` or `bettercam`
- Runs frame through ONNX model (e.g. YOLO)
- Filters detections via NMS
- Moves mouse for aim assist
- Renders bounding boxes using OpenCV (no overlay script required)

## ❗ Important Notes
- This software is intended as an **assistive tool** for gamers with physical or cognitive impairments.
- Part of the nonprofit initiative by **FNBubbles420 Org**, a registered 501(c)(3) charity.

## 🙌 Support & Community
Need help? Have feedback? Join our Discord:
👉 [https://discord.gg/9vG777kJYc](https://discord.gg/9vG777kJYc)

Ping `Bubbles` for assistance or questions.

---
© 2025 FNBubbles420 Org. All Rights Reserved.
