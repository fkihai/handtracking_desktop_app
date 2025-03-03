import cv2
import imutils
from imutils.video import VideoStream


class Camera :
    
    def __init__(self,cap_index):
        self.cap = VideoStream(cap_index).start()
        if self.cap is None:
            print(f"❌ Kamera {cap_index} tidak bisa dibuka!")
            self.cap = None
            
    def get_frame(self):        
        if self.cap:
            return self.cap.read()
        
        return False, None
    
    def release(self):
        if self.cap:
            self.cap.stop()
   
   