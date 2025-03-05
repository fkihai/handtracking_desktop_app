import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MatplotlibCanvas(FigureCanvas):
    
    def __init__(self, n=100):
        self.figure, self.ax = plt.subplots(8,1)
        super().__init__(self.figure)
        
        self.n = n
        self.x = np.arange(n)
        self.data = np.zeros((8, n))

        # Inisialisasi garis plot untuk 8 channel
        self.list_color  = ['cyan', 'orange', 'lime', 'red', 'magenta', 'yellow', 'blue', 'white']
        self.lines = [ax.plot(self.x, self.data[i],self.list_color[i])[0] for i, ax in enumerate(self.ax)]
       
        for axis in self.ax:
            axis.set_facecolor((36/255, 31/255, 49/255))
            axis.set_ylim([-100, 100])
            axis.set_xticks([])
            axis.set_yticks([])
        
        self.figure.patch.set_facecolor((36/255, 31/255, 49/255))
        self.figure.subplots_adjust(
            left=0.01, right=0.99, top=0.99, bottom=0.01,
            wspace=0.1, hspace=0.3
        )


    def update_plot(self, emg_data):
        emg_data = np.array(emg_data)
        self.data = np.roll(self.data, -1, axis=1)
        self.data[:, -1] = emg_data[:, -1]
        
        for i in range(8):
            self.lines[i].set_ydata(self.data[i])
        self.figure.canvas.draw_idle()
        

