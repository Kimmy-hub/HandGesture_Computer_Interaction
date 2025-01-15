import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def detect_gesture(landmarks):
    """
    Detects hand gestures based on the positions of hand landmarks.
    """
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
    thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP].y
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_up = thumb_tip < thumb_ip
    index_up = index_tip < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_up = middle_tip < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_up = ring_tip < landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_up = pinky_tip < landmarks[mp_hands.HandLandmark.PINKY_PIP].y

    fingers_up = sum([index_up, middle_up, ring_up, pinky_up])

    if thumb_up and fingers_up == 0:
        return "Thumbs Up"
    elif not thumb_up and fingers_up == 0:
        return "Thumbs Down"
    elif thumb_up and fingers_up == 4:
        return "Open Hand"
    elif fingers_up == 2:
        return "2 Fingers"
    elif fingers_up == 3:
        return "3 Fingers"
    else:
        return "Unknown Gesture"

cap = cv2.VideoCapture(0)

current_gesture = None
gesture_start_time = None
gesture_confirmation_time = {
    "Open Hand": 1, 
    "2 Fingers": 1, 
    "3 Fingers": 1,  
    "Thumbs Up": 0, 
    "Thumbs Down": 0,  
}

try:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        frame = cv2.flip(frame, 1)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                gesture = detect_gesture(hand_landmarks.landmark)
                
                cv2.putText(frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                if gesture != current_gesture:
                    current_gesture = gesture
                    gesture_start_time = time.time()  

                if current_gesture in gesture_confirmation_time:
                    required_time = gesture_confirmation_time[current_gesture]
                    if time.time() - gesture_start_time >= required_time:
                        if current_gesture == "Open Hand":
                            pyautogui.press('playpause')  
                        elif current_gesture == "2 Fingers":
                            pyautogui.hotkey('alt', 'tab') 
                        elif current_gesture == "3 Fingers":
                            pyautogui.hotkey('prtscr')  
                        elif current_gesture == "Thumbs Up":
                            pyautogui.press('volumeup')  
                        elif current_gesture == "Thumbs Down":
                            pyautogui.press('volumedown')  

                        current_gesture = None
                        gesture_start_time = None

        cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()