import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
from threading import Lock, Thread
import cv2
import mediapipe as mp
import math
import warnings
from scipy.interpolate import interp1d
import csv

# Nonaktifkan peringatan Protobuf yang tidak perlu
warnings.filterwarnings('ignore', category=UserWarning, module='google.protobuf')
#200 samples x 30 detik untuk data target
seconds = 59
target_samples = seconds * 200
data_target_samples = target_samples
collectt=True
# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk menghitung sudut antara tiga titik
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    # Menghitung vektor
    ba = a - b
    bc = c - b

    # Menghitung dot product dan norm
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)

    # Menghitung sudut
    angle = np.degrees(np.arccos(cosine_angle))

    return angle

# Fungsi untuk mengumpulkan sudut dari webcam dan menyimpannya ke CSV
def collect_angle_data():
    global collectt
    cap = cv2.VideoCapture(2)
    angle_data = []

    # Tulis header di sini
    header = ['Time', 'Thumb_CMC', 'Thumb_MCP', 'Thumb_IP', 'Index_MCP', 'Index_PIP', 'Index_DIP', 
              'Middle_MCP', 'Middle_PIP', 'Middle_DIP', 'Ring_MCP', 'Ring_PIP', 'Ring_DIP', 
              'Pinky_MCP', 'Pinky_PIP', 'Pinky_DIP']

    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        start_time = time.time()
        print('========= Mulai Mengumpulkan Sudut =========')
        while cap.isOpened() and collectt:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    landmarks = hand_landmarks.landmark
                    h, w, c = frame.shape

                    def get_coord(landmark):
                        return [int(landmarks[landmark].x * w), int(landmarks[landmark].y * h)]

                    # Dictionary untuk setiap jari dan sudutnya
                    fingers = {
                        "Thumb": [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.THUMB_CMC,
                                  mp_hands.HandLandmark.THUMB_MCP, mp_hands.HandLandmark.THUMB_IP,
                                  mp_hands.HandLandmark.THUMB_TIP],
                        "Index": [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.INDEX_FINGER_MCP,
                                  mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.INDEX_FINGER_DIP,
                                  mp_hands.HandLandmark.INDEX_FINGER_TIP],
                        "Middle": [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                                   mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
                                   mp_hands.HandLandmark.MIDDLE_FINGER_DIP,
                                   mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                        "Ring": [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.RING_FINGER_MCP,
                                 mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.RING_FINGER_DIP,
                                 mp_hands.HandLandmark.RING_FINGER_TIP],
                        "Pinky": [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.PINKY_MCP,
                                  mp_hands.HandLandmark.PINKY_PIP, mp_hands.HandLandmark.PINKY_DIP,
                                  mp_hands.HandLandmark.PINKY_TIP]
                    }

                    # Tempatkan nilai sudut untuk setiap jari
                    row = []
                    row.append(time.time() - start_time)  # Timestamp
                    for finger_name, joints in fingers.items():
                        if finger_name == "Thumb":
                            print('THUMB')
                            cmc = get_coord(joints[1])
                            mcp = get_coord(joints[2])
                            ip = get_coord(joints[3])
                            tip = get_coord(joints[4])

                            wrist = get_coord(joints[0])
                            cmc_angle = calculate_angle(wrist, cmc, mcp)
                            mcp_angle = calculate_angle(cmc, mcp, ip)
                            ip_angle = calculate_angle(mcp, ip, tip)

                            # Tampilkan sudut di frame
                            if not np.isnan(cmc_angle):
                                cv2.putText(frame, f'{int(cmc_angle)}', tuple(cmc), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
                            if not np.isnan(mcp_angle):
                                cv2.putText(frame, f'{int(mcp_angle)}', tuple(mcp), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
                            if not np.isnan(ip_angle):
                                cv2.putText(frame, f'{int(ip_angle)}', tuple(ip), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

                            # Masukkan sudut ke row
                            row.append(cmc_angle)
                            row.append(mcp_angle)
                            row.append(ip_angle)

                        else:
                            print('BUKAN THUMB')
                            wrist = get_coord(joints[0])
                            mcp = get_coord(joints[1])
                            pip = get_coord(joints[2])
                            dip = get_coord(joints[3])
                            tip = get_coord(joints[4])

                            mcp_angle = calculate_angle(wrist, mcp, pip)
                            pip_angle = calculate_angle(mcp, pip, dip)
                            dip_angle = calculate_angle(pip, dip, tip)

                            # Tampilkan sudut di frame
                            if not np.isnan(mcp_angle):
                                cv2.putText(frame, f'{int(mcp_angle)}', tuple(mcp), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
                            if not np.isnan(pip_angle):
                                cv2.putText(frame, f'{int(pip_angle)}', tuple(pip), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                            if not np.isnan(dip_angle):
                                cv2.putText(frame, f'{int(dip_angle)}', tuple(dip), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

                            # Masukkan sudut ke row
                            row.append(mcp_angle)
                            row.append(pip_angle)
                            row.append(dip_angle)
                            

                    # Tambahkan data sudut ke dalam list
                    angle_data.append(row)
                    

            # Tampilkan hasil frame
            cv2.imshow('Hand Tracking', frame)

            elapsed_time = time.time() - start_time
            t = int(elapsed_time)
            if t in [0, 15, 30, 45, 60, 75]:
                print('      =======> GENGGAM <========', end='\r')
            elif t in [5, 20, 35, 50, 65, 80]:
                print('      =========> LEPASKAN <========', end='\r')
            elif t in [10, 25, 40, 55, 70, 85]:
                print('      =========> ISTIRAHAT <========', end='\r')

            if elapsed_time >= seconds:
                collectt = False
                break

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    print("======== Pengumpulan Sudut Berhenti ========")
    
    # Setelah pengumpulan selesai, simpan data ke dalam DataFrame dan CSV
    # print(angle_data)
    angle_df = pd.DataFrame(angle_data, columns=header)
    # angle_df.to_csv('angle_data.csv', index=False)

    # Upsampling ke 1800 nilai
    target_length = data_target_samples

    # Membuat array baru untuk indeks target
    new_index = np.linspace(0, len(angle_df) - 1, target_length)

    # Menggunakan interp1d untuk interpolasi
    upsampled_data = {}
    for column in angle_df.columns[1:]:  # Mengambil semua kolom kecuali 'Time'
        f = interp1d(np.arange(len(angle_df)), angle_df[column], kind='linear', fill_value="extrapolate")
        upsampled_data[column] = f(new_index)

    # Membuat DataFrame baru dari data yang di-interpolasi
    upsampled_df = pd.DataFrame(upsampled_data)

    # Menyimpan DataFrame yang di-interpolasi ke CSV
    # upsampled_df.to_csv('Prog_tesis\Data_collect_Cam_Myo\data_landmark.csv', index=False)


if __name__ == '__main__':
    collect_angle_data()
