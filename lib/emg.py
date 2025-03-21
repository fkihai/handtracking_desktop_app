import myo
import numpy as np
from threading import Lock
from PyQt5.QtCore import QThread, pyqtSignal
from collections import deque
from datetime import datetime
import time

# Dummy 
class EmgCollector(myo.DeviceListener):
    def __init__(self, n):
        super().__init__()
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
                if isinstance(data[0], str) and isinstance(data[1], list):
                    return [data[0]] + data[1] 
                return data[1]  
            return None


    def get_list_emg_data(self):
        with self.lock:
            return list(self.emg_data_queue)
    
    def get_list_emg_full_data(self):
        return list(self.emg_full_data)
    
    def on_connected(self, event):
        event.device.stream_emg(True)

    def on_emg(self, event):
        timestamp = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S") 
        emg_data = list(event.emg)  

        with self.lock:
            self.emg_data_queue.append((timestamp, emg_data))
            if self.record:
                self.emg_full_data.append((timestamp, emg_data)) 
                
                       
class EmgThread(QThread):
    data_updated = pyqtSignal(list)
    
    def __init__(self, listener):
        super().__init__()
        self.listener = listener
        self.running = True
        
    def run(self):
        myo.init()
        hub = myo.Hub()
        with hub.run_in_background(self.listener):
            while self.running:
                emg_data = self.listener.get_list_emg_data()
                if  emg_data:
                    emg_data = np.array([x[1] for x in emg_data]).T
                    self.data_updated.emit(emg_data.tolist())
                self.msleep(100)
    
    def stop(self):
        self.running = False
        self.quit()
        self.wait()