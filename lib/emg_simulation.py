import numpy as np
import time
from datetime import datetime
from threading import Lock
from PyQt5.QtCore import QThread, pyqtSignal
from collections import deque

# Dummy 
class EmgCollector:
    def __init__(self, n):
        self.n = n
        self.lock = Lock()
        self.record = False
        self.emg_full_data = []
        self.emg_data_queue = deque(maxlen=n)

    def start_recording(self):
        self.emg_full_data = []
        self.record = True
    
    def stop_recording(self):
        self.record = False
        
    def get_emg(self):
        with self.lock:
            if self.emg_data_queue:
                data = self.emg_data_queue[-1]
                if isinstance(data[0], str) and isinstance(data[1].tolist(), list):
                    return [data[0]] + data[1].tolist() 
                return data[1]  
            return None

    def get_list_emg_data(self):
        with self.lock:
            return list(self.emg_data_queue)
    
    def get_list_emg_full_data(self):
        return list(self.emg_full_data)

    def generate_dummy_emg(self):
        timestamp = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S") 
        dummy_emg = np.random.randint(-100, 100, size=8)
        with self.lock:
            self.emg_data_queue.append((timestamp, dummy_emg))
            if self.record :
                self.emg_full_data.append((timestamp,dummy_emg))
                          
class EmgThread(QThread):
    data_updated = pyqtSignal(list)
    
    def __init__(self, listener):
        super().__init__()
        self.listener = listener
        self.running = True
        
    def run(self):
        while self.running:
            self.listener.generate_dummy_emg()
            emg_data = self.listener.get_list_emg_data()
            emg_data = np.array([x[1] for x in emg_data]).T 
            self.data_updated.emit(emg_data.tolist())
            self.msleep(100)
    
    def stop(self):
        self.running = False
        self.quit()
        self.wait()