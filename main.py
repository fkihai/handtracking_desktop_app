from PyQt5.QtWidgets import QApplication, QMainWindow, QBoxLayout
from PyQt5.QtCore import QTimer,QThread
from gui import Ui_MainWindow
from lib.camera import Camera

from lib.hand_tracking import HandTracking
from lib.camera_thread import CameraThread
from lib.plot_view import PlotWidget
from lib.emg import EmgCollector, EmgThread
from lib.canvas import MatplotlibCanvas

from datetime import datetime
import pandas as pd
import sys
import os



class MainApp(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.camera = Camera(2)
        self.hand_tracking = HandTracking()
        
        # thread camera
        self.camera_thread = CameraThread(self.camera,self.hand_tracking)
        self.camera_thread.frame_updated.connect(self.update_frame_camera)
        self.camera_thread.start()
        
        # Emg
        self.emg_listener = EmgCollector(n=100)
        self.emg_thread = EmgThread(self.emg_listener)
        self.emg_thread.data_updated.connect(self.show_data)
        self.emg_thread.start()
              
        # save landmark
        self.header = ['Time', 'Thumb_CMC', 'Thumb_MCP', 'Thumb_IP', 'Index_MCP', 'Index_PIP', 'Index_DIP', 
            'Middle_MCP', 'Middle_PIP', 'Middle_DIP', 'Ring_MCP', 'Ring_PIP', 'Ring_DIP', 
            'Pinky_MCP', 'Pinky_PIP', 'Pinky_DIP']
        self.data_landmark = []
        
        # Perintah
        self.cmd_timer = QTimer(self)
        self.cmd_timer.timeout.connect(self.update_perintah)
        self.index_cmd = 0
        self.list_cmd = ['Genggam','Lepaskan','Istirahat']
        
        # state mode
        self.collect = False
        self.realtime = False
        self.training = False
        
        # widget state mmode
        self.list_mode = ['Collect','Realtime','Training']
        self.choose_mode.addItems(self.list_mode)
        self.pb_start_mode.clicked.connect(self.startMode)
        self.pb_stop_mode.clicked.connect(self.stopMode)
        self.pb_stop_mode.setEnabled(False)
        
        # plot widget
        self.canvas = MatplotlibCanvas()
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.canvas)
        self.plot_view.setLayout(layout)  
        
        
        self.timer = QTimer()
        self.timer.setInterval(100) 
        self.timer.timeout.connect(self.canvas.update_plot)
        self.timer.start()
        
        
        # self.plot = PlotWidget()
        # self.frame_plot = self.plot.plot_graph().scaled(self.plot_view.width(),self.plot_view.height())
        # self.plot_view.setPixmap(self.frame_plot)
        # self.error_view.setPixmap(self.frame_plot) 
        
    
    def show_data(self,list):
        # print(f"ini data emg : {type(list)}")   
        pass  
            
    def update_frame_camera(self,frame):
        pixmap = frame
        pixmap = pixmap.scaled(self.camera_view.width(),self.camera_view.height())
        self.camera_view.setPixmap(pixmap)
        
        # save data landmark
        data_row = self.hand_tracking.get_landmark_data()
        
        if self.collect :
            if not data_row:
                return
        
            self.data_landmark.append(self.hand_tracking.get_landmark_data())
        
    def save_data_landmark(self):
        
        save_folder = 'data'
        os.makedirs(save_folder,exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_folder, f'landmark_{timestamp}.csv')
        file_exists = os.path.isfile(file_path)
        
        if not self.data_landmark:
            print("Data Landmark Empty")    
            return
                    
        df = pd.DataFrame(self.data_landmark, columns=self.header)
        df.to_csv(file_path, mode='a', index=False, header=not file_exists)
        print("save data landmark successfully")
        
       
    def startMode(self):
        mode = self.choose_mode.currentText()
        self.radioButton_active.setChecked(True)
        self.pb_stop_mode.setEnabled(True)
        self.pb_start_mode.setEnabled(False)
        
        if mode == self.list_mode[0]:
            self.collect, self.realtime, self.training = True, False, False
            if self.collect :
                    QTimer.singleShot(1000, self.update_perintah) # delay awal

        elif mode == self.list_mode[1]:
            self.collect, self.realtime, self.training = False, True, False
            
        else :
            self.collect, self.realtime, self.training = False, False, True
            
    
    def stopMode(self):
        self.pb_stop_mode.setEnabled(False)
        self.pb_start_mode.setEnabled(True)
        
        if self.collect:
            self.save_data_landmark()
            self.collect = False
            
        self.cmd_timer.stop()
        self.cmd_view.setText("")
        self.radioButton_active.setChecked(False)

        
    def update_perintah(self):
    
        self.cmd_view.setText(self.list_cmd[self.index_cmd])
        self.index_cmd = (self.index_cmd + 1) % len(self.list_cmd) 
        self.cmd_timer.start(5000)
        

    #  event handler bawaan
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
    
    
    
