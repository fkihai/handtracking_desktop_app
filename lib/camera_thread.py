import cv2
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

class CameraThread(QThread):
    frame_updated = pyqtSignal(QPixmap)
    
    def __init__(self, camera, hand_tracking):
        super().__init__()
        self.camera = camera
        self.hand_tracking = hand_tracking
        self.running = True

    def run(self):
        while self.running:
            frame = self.camera.get_frame()
            if frame is not None:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = self.hand_tracking.tracking(frame)
                height, width, channel = frame.shape
                qimg = QImage(frame.data, width, height, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                               
                self.frame_updated.emit(pixmap)  
            else :
                print('camera error. camera not available')

    def stop(self):
        self.running = False
        self.quit()
        self.wait()