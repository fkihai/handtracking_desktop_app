import os
import sys
import time
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QBoxLayout
from PyQt5.QtCore import QTimer,Qt

from gui import Ui_MainWindow
from lib.camera import Camera
from lib.hand_tracking import HandTracking
from lib.camera_thread import CameraThread
from lib.emg import EmgCollector, EmgThread
from lib.plot_canvas import MatplotlibCanvas
from datetime import datetime as dt


# TODO:
# Membuat download semuad data record

class MainApp(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.camera = Camera(2)
        self.hand_tracking = HandTracking()
        self.canvas = MatplotlibCanvas()
        self.emg_listener = EmgCollector(n=500)

        # data buffer
        self.landmark_buffer = []
        self.emg_buffer = []
        self.latest_frame = None 
        
        # counter cmd 
        self.index_cmd = 0
        
        # state mode
        self.collect = False
        self.realtime = False
        self.training = False
        self.list_mode = ['Collect','Realtime','Training']

        # camera thread
        self.camera_thread = CameraThread(self.camera,self.hand_tracking)
        self.camera_thread.frame_updated.connect(self.update_frame_camera,Qt.QueuedConnection)
        self.camera_thread.start()

        # Emg thread
        self.emg_thread = EmgThread(self.emg_listener)
        self.emg_thread.data_updated.connect(self.canvas.update_plot)
        self.emg_thread.start()

        # Perintah
        self.cmd_timer = QTimer(self)
        self.cmd_timer.timeout.connect(self.update_perintah)

        # widget state mmode
        self.choose_mode.addItems(self.list_mode)
        self.pb_start_mode.clicked.connect(self.startMode)
        self.pb_stop_mode.clicked.connect(self.stopMode)
        self.pb_stop_mode.setEnabled(False)
        
        # plot widget
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.canvas)
        self.plot_view.setLayout(layout)
    
    
    def store_emg(self, emg_data):
        self.emg_buffer = emg_data
        
    def update_plot(self):
        if self.emg_buffer:
            self.canvas.update_plot(self.emg_buffer)

    def update_frame_camera(self,frame):

        pixmap = frame
        pixmap = pixmap.scaled(self.camera_view.width(),self.camera_view.height())
        self.camera_view.setPixmap(pixmap)
    
        data_row = self.hand_tracking.get_landmark_data()
        if self.collect :
            if not data_row:
                return
            self.landmark_buffer.append(data_row)
       
    def startMode(self):
        mode = self.choose_mode.currentText()
        self.radioButton_active.setChecked(True)
        self.pb_stop_mode.setEnabled(True)
        self.pb_start_mode.setEnabled(False)
        
        if mode == self.list_mode[0]:
            self.collect, self.realtime, self.training = True, False, False
            if self.collect :
                    self.emg_listener.start_recording()
                    QTimer.singleShot(1000, self.update_perintah) # delay awal

        elif mode == self.list_mode[1]:
            self.collect, self.realtime, self.training = False, True, False
            
        else :
            self.collect, self.realtime, self.training = False, False, True
            
    
    def stopMode(self):
        self.pb_stop_mode.setEnabled(False)
        self.pb_start_mode.setEnabled(True)
        
        if self.collect:
            self.save_landmark()
            self.save_myo()
            
            self.emg_listener.stop_recording()
            self.collect = False
                    
        self.cmd_timer.stop()
        self.cmd_view.setText("")
        self.radioButton_active.setChecked(False)

        
    def update_perintah(self):
        list_cmd = ['Genggam','Lepaskan','Istirahat']
        self.cmd_view.setText(list_cmd[self.index_cmd])
        self.index_cmd = (self.index_cmd + 1) % len(list_cmd) 
        self.cmd_timer.start(5000)
        
        
    def save_landmark(self):
        
        header_landmark = ['Time', 'Thumb_CMC', 'Thumb_MCP', 'Thumb_IP', 'Index_MCP', 'Index_PIP', 'Index_DIP', 
        'Middle_MCP', 'Middle_PIP', 'Middle_DIP', 'Ring_MCP', 'Ring_PIP', 'Ring_DIP', 
        'Pinky_MCP', 'Pinky_PIP', 'Pinky_DIP']
        
        os.makedirs(os.path.join('data','landmark'), exist_ok=True)
        landmark_file_path = os.path.join('data', 'landmark', f'landmark_{dt.now().strftime("%Y%m%d_%H%M%S")}.csv')
        
        if not self.landmark_buffer:
            print("Data Landmark Empty")    
            return
        
        # save csv landmark
        df_landmark = pd.DataFrame(self.landmark_buffer, columns=header_landmark)
        df_landmark.to_csv(landmark_file_path, mode='a', index=False)
        
        # reset data after save
        self.hand_tracking.reset_row()
        self.landmark_buffer = []  
    
    def save_myo(self):
        
        header_myo = ["EMG_1", "EMG_2", "EMG_3", "EMG_4", "EMG_5", "EMG_6", "EMG_7", "EMG_8"]
                
        os.makedirs(os.path.join('data','myo'), exist_ok=True)
        myo_file_path = os.path.join('data','myo',f'myo_{dt.now().strftime("%Y%m%d_%H%M%S")}.csv')
        
        emg_data = self.emg_listener.get_emg_full_data()
        emg_data = np.array([x[1] for x in emg_data]).T
                
        df_myo =  pd.DataFrame(emg_data.T,columns=header_myo)
        df_myo.to_csv(myo_file_path, mode='a', index=False)

        
    def closeEvent(self, event):
        self.camera_thread.stop()
        if self.camera:
            self.camera.release()
            print('Tutup')
        event.accept()           
             
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
    
    
    
