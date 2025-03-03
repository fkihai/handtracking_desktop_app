from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QThread, pyqtSignal
from collections import deque
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np


# Dummy 
class EmgCollector:
    def __init__(self, n):
        self.n = n
        self.emg_data_queue = deque(maxlen=n)

    def get_emg_data(self):
        return list(self.emg_data_queue)

    def generate_dummy_emg(self):
        """Simulasi data EMG acak antara -100 sampai 100"""
        dummy_emg = np.random.randint(-100, 100, size=8)
        self.emg_data_queue.append((0, dummy_emg))  # Timestamp tidak dipakai



class EmgThread(QThread):
    data_updated = pyqtSignal(list)
    
    def __init__(self, listener):
        super().__init__()
        self.listener = listener
        self.running = True
        
    def run(self):
        while self.running:
            self.listener.generate_dummy_emg()
            emg_data = self.listener.get_emg_data()
            emg_data = np.array([x[1] for x in emg_data]).T 
            self.data_updated.emit(emg_data.tolist())
            self.msleep(100)
    
    def stop(self):
        self.running = False
        self.quit()
        self.wait()


# class EmgCollector(myo.DeviceListener):
#     def __init__(self, n):
#         self.n = n

#     def get_emg_data(self):
#         with self.lock:
#             return list(self.emg_data_queue)

#     def on_connected(self, event):
#         event.device.stream_emg(True)

#     def on_emg(self, event):
#         with self.lock:
#             self.emg_data_queue.append((event.timestamp, event.emg))