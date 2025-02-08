# Hand Gesture Control for PC  

This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to recognize hand gestures via webcam and perform actions like controlling media, switching applications, and adjusting volume.  

## Features  
- 🎵 **Media Control**: Play/Pause music with an open hand gesture.  
- 🔄 **App Switching**: Switch between open applications using a two-finger gesture.  
- 📸 **Screenshot Capture**: Take a screenshot with a three-finger gesture.  
- 🔊 **Volume Control**: Adjust volume using thumbs-up or thumbs-down gestures.  

## Installation  

### 1️⃣ Install Dependencies  
Make sure Python is installed, then run:  
```sh
pip install opencv-python mediapipe pyautogui
```

### 2️⃣ Run the Script  
```sh
python gesture_control.py
```

## Gesture Actions  

| Gesture       | Action               |
|--------------|----------------------|
| 👍 Thumbs Up | Volume Up            |
| 👎 Thumbs Down | Volume Down        |
| ✋ Open Hand | Play/Pause Media     |
| ✌️ Two Fingers | Switch Application |
| 🤞 Three Fingers | Take Screenshot |

## Usage  
1. Run the script.  
2. Allow access to the webcam.  
3. Perform hand gestures to trigger different actions.  
4. Press `Esc` to exit.  

## Dependencies  
- **Python 3.x**  
- **OpenCV**  
- **MediaPipe**  
- **PyAutoGUI**  

## Future Improvements  
- ✨ Add more gestures for additional functionalities.  
- 📱 Extend support for mobile control via ADB.  
- 🖱️ Implement cursor control using hand tracking.  

## License  
This project is open-source under the **MIT License**.  

---

Made with ❤️ using Python. 🚀  
