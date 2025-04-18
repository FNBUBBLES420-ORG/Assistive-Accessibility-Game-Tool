from win32con import VK_RBUTTON

# Screen capture settings
screenShotHeight = 320  # Height of the screen portion to capture
screenShotWidth = 320   # Width of the screen portion to capture

# Mask settings (useful for hiding interfering objects like player models or weapons)
useMask = True          # Enable or disable masking
maskSide = "left"       # Side of the mask: "left" or "right"
maskWidth = 140         # Width of the mask
maskHeight = 240        # Height of the mask

# Autoaim settings
aaMovementAmp = 1.0     # Mouse movement amplifier (range: 0.1–5.0)
aaQuitKey = "8"         # Key to quit and shut down autoaim
aaActivationKey = VK_RBUTTON  # Key to toggle autoaim (default: right mouse button)
headshot_mode = True    # Aim slightly upwards for headshots

# Confidence threshold
confidence = 0.72    # Confidence threshold for detection (0.1–1.0)

# Serial communication settings (e.g., for Arduino)
enableSerial = True         # Enable or disable serial communication
fallbackSerialPort = "COM3" # Fallback COM port (e.g., COM3 for Windows)
baudRate = 115200           # Baud rate (must match Arduino sketch)

# Display settings
cpsDisplay = True   # Show corrections per second (CPS) in the terminal
visuals = True   # Enable or disable visualizations (e.g., bounding boxes, FPS) If you have a low-end GPU, disable this option to improve FPS.
# Target selection settings
centerOfScreen = True  # Smarter selection of people based on screen center

# ONNX model settings
onnxProvider = 'CUDAExecutionProvider'  # Options: 'CUDAExecutionProvider', 'DmlExecutionProvider', 'CPUExecutionProvider'
model_path = 'onnx-models/v5_mini_royale.onnx'  # Path to the ONNX model
device = 'cuda'  # Device for inference: 'cuda' (NVIDIA GPU) or 'cpu' (AMD or no GPU)
fp16 = True      # Use FP16 for faster inference (set to False for AMD GPUs)