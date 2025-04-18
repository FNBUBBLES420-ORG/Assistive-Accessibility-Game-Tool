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
- Make sure `READ` & install all required packages by reading the `requirements.txt` file. 
- Follow Directions

## 🚀 NVIDIA Setup Instructions

### Step 1: Install CUDA 11.8
Download from: https://developer.nvidia.com/cuda-11-8-0-download-archive
Run the `.exe` installer and make sure the following components are selected:
- CUDA Toolkit
- CUDA Samples
- Visual Studio Integration (optional)
- CUDA Documentation (optional)

### Step 2: Reboot After Installation
Restart your computer after installing CUDA Toolkit.

### Step 3: Install cuDNN
Download cuDNN from: https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.6/local_installers/
Unzip it and move all contents into your CUDA directory:
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8
```
Replace any existing files if prompted.

### Step 4: Install TensorRT
Download TensorRT from: https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/secure/
Extract and copy all folders/files into the same CUDA directory:
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8
```
Then run the following command:
```bash
pip install "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\python\tensorrt-8.6.1-cp311-none-win_amd64.whl"
```
Make sure the `.whl` matches your Python version (`cp311` = Python 3.11).

### Step 5: Install CuPy for CUDA 11.8
```bash
pip install cupy-cuda11x
```

### Step 6: Add Environment Variables
Add the following paths to your system's environment variables:
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib
```

### Step 7: Verify GPU Availability in Python
Run the following in a Python shell:
```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```
This will confirm your GPU setup is recognized by PyTorch.

### Step 8: Install Visual Studio 2022
NVIDIA users must also install **Visual Studio 2022 Community Edition** to support compiler integration:
[Download VS 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/)
- Select "Desktop development with C++" during installation

---

## 🔦 AMD Setup Instructions

AMD users must also install **Visual Studio 2022 Community Edition**.

### Step 1: Download Visual Studio 2022
[Download VS 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/)

### Step 2: Install Desktop Development with C++
In the installer:
- Select "Desktop development with C++"
- Install

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
# uncomment if you have Nvidia gpu below 👇 
# onnxruntime-gpu==1.17.0 # This is correct for this application 
onnxruntime-directml==1.17.0
opencv-python>==4.8.1.78
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
onnx-simplifier
dill
serial
pyserial
pyarmor
# DirectML dependencies for Windows AMD GPUs
# torch-directml
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

## Sceenshots
<img src="https://github.com/FNBUBBLES420-ORG/Assistive-Accessibility-Game-Tool/blob/main/image-1.png" width="350">

## ❗ Important Notes
- This software is intended as an **assistive tool** for gamers with physical or cognitive impairments.
- Part of the nonprofit initiative by **FNBubbles420 Org**, a registered 501(c)(3) charity.

## 🙌 Support & Community
Need help? Have feedback? Join our Discord:
👉 [https://discord.gg/9vG777kJYc](https://discord.gg/9vG777kJYc)

Ping `Bubbles` for assistance or questions.

---
© 2025 FNBubbles420 Org. All Rights Reserved.
