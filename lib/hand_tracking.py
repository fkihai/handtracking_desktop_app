
from lib.camera import Camera
from datetime import datetime
from collections import deque
import mediapipe as mp
import numpy as np
import pandas as pd
import time
import cv2
import os

class HandTracking():
    
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.frame = None
        
        # save data landmark
        self.row = deque(maxlen=100)

    def reset_row (self):
        self.row = []

    def calculate_angle(self,a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        cosine_angle = np.clip(cosine_angle, -1.0, 1.0)
        angle = np.degrees(np.arccos(cosine_angle))
        return angle
    
    
    def tracking(self, frame):             
        self.frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(self.frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                landmarks = hand_landmarks.landmark
                h, w, c = self.frame.shape
                
                def get_coord(landmark):
                        return [int(landmarks[landmark].x * w), int(landmarks[landmark].y * h)]
                
                fingers = {
                        "Thumb": [self.mp_hands.HandLandmark.WRIST, self.mp_hands.HandLandmark.THUMB_CMC,
                                  self.mp_hands.HandLandmark.THUMB_MCP, self.mp_hands.HandLandmark.THUMB_IP,
                                  self.mp_hands.HandLandmark.THUMB_TIP],
                        "Index": [self.mp_hands.HandLandmark.WRIST, self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
                                  self.mp_hands.HandLandmark.INDEX_FINGER_PIP, self.mp_hands.HandLandmark.INDEX_FINGER_DIP,
                                  self.mp_hands.HandLandmark.INDEX_FINGER_TIP],
                        "Middle": [self.mp_hands.HandLandmark.WRIST, self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                                   self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
                                   self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP,
                                   self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                        "Ring": [self.mp_hands.HandLandmark.WRIST, self.mp_hands.HandLandmark.RING_FINGER_MCP,
                                 self.mp_hands.HandLandmark.RING_FINGER_PIP, self.mp_hands.HandLandmark.RING_FINGER_DIP,
                                 self.mp_hands.HandLandmark.RING_FINGER_TIP],
                        "Pinky": [self.mp_hands.HandLandmark.WRIST, self.mp_hands.HandLandmark.PINKY_MCP,
                                  self.mp_hands.HandLandmark.PINKY_PIP, self.mp_hands.HandLandmark.PINKY_DIP,
                                  self.mp_hands.HandLandmark.PINKY_TIP]
                    }
                                
                self.row = []
                timestamp = time.time()
                formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                self.row.append(formatted_time)
                    
                for finger_name, joints in fingers.items():
                    if finger_name == "Thumb":
                        cmc = get_coord(joints[1])
                        mcp = get_coord(joints[2])
                        ip = get_coord(joints[3])
                        tip = get_coord(joints[4])

                        wrist = get_coord(joints[0])
                        cmc_angle = self.calculate_angle(wrist, cmc, mcp)
                        mcp_angle = self.calculate_angle(cmc, mcp, ip)
                        ip_angle = self.calculate_angle(mcp, ip, tip)

                        # Tampilkan sudut di frame
                        if not np.isnan(cmc_angle):
                            cv2.putText(self.frame, f'{int(cmc_angle)}', tuple(cmc), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
                        if not np.isnan(mcp_angle):
                            cv2.putText(self.frame, f'{int(mcp_angle)}', tuple(mcp), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
                        if not np.isnan(ip_angle):
                            cv2.putText(self.frame, f'{int(ip_angle)}', tuple(ip), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

                        # save angle thumb
                        self.row.append(cmc_angle)
                        self.row.append(mcp_angle)
                        self.row.append(ip_angle)

                    else:
                        wrist = get_coord(joints[0])
                        mcp = get_coord(joints[1])
                        pip = get_coord(joints[2])
                        dip = get_coord(joints[3])
                        tip = get_coord(joints[4])

                        mcp_angle = self.calculate_angle(wrist, mcp, pip)
                        pip_angle = self.calculate_angle(mcp, pip, dip)
                        dip_angle = self.calculate_angle(pip, dip, tip)

                        # Tampilkan sudut di frame
                        if not np.isnan(mcp_angle):
                            cv2.putText(self.frame, f'{int(mcp_angle)}', tuple(mcp), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
                        if not np.isnan(pip_angle):
                            cv2.putText(self.frame, f'{int(pip_angle)}', tuple(pip), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                        if not np.isnan(dip_angle):
                            cv2.putText(self.frame, f'{int(dip_angle)}', tuple(dip), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
                                                
                        # save angle
                        self.row.append(mcp_angle)
                        self.row.append(pip)
                        self.row.append(dip_angle)     
                                              
        return self.frame


    def get_landmark_data(self):
        return self.row