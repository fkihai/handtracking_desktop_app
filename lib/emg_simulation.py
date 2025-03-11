import numpy as np
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

    def get_emg_data(self):
        with self.lock:
            return list(self.emg_data_queue)
    
    def get_emg_full_data(self):
        return list(self.emg_full_data)

    def generate_dummy_emg(self):
        dummy_emg = np.random.randint(-100, 100, size=8)
        with self.lock:
            self.emg_data_queue.append((0, dummy_emg))
            if self.record :
                self.emg_full_data.append((0,dummy_emg))
                          
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