import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MatplotlibCanvas(FigureCanvas):
    
    def __init__(self):
        self.figure, self.ax = plt.subplots(8,1)
        super().__init__(self.figure)
        
        self.x = np.linspace(0,10,100)
        self.t = 0.0
        
        self.line1, = self.ax[0].plot(self.x, np.sin(self.x + self.t))
        self.line2, = self.ax[1].plot(self.x, np.cos(self.x + self.t))
        self.line3, = self.ax[2].plot(self.x, np.tan(self.x + self.t))
        self.line4, = self.ax[3].plot(self.x, np.sinh(self.x + self.t))
        self.line5, = self.ax[4].plot(self.x, np.cosh(self.x + self.t))
        self.line6, = self.ax[5].plot(self.x, np.tanh(self.x + self.t))
        self.line7, = self.ax[6].plot(self.x, np.sin(self.x + self.t) * np.cos(self.x + self.t))
        self.line8, = self.ax[7].plot(self.x, np.sin(self.x + self.t) + np.cos(self.x + self.t))
        
        
        for axis in self.ax:
            axis.set_facecolor((36/255, 31/255, 49/255))
            axis.set_xticks([])
            axis.set_yticks([])
        
        self.figure.patch.set_facecolor((36/255, 31/255, 49/255))
        self.figure.subplots_adjust(
            left=0.01, right=0.99, top=0.99, bottom=0.01,
            wspace=0.1, hspace=0.3
        )
    
    def update_plot(self):
        
        self.t += 0.1
        
        self.line1.set_ydata(np.sin(self.x + self.t))
        self.line2.set_ydata(np.cos(self.x + self.t))
        self.line3.set_ydata(np.sin(self.x + self.t))
        self.line4.set_ydata(np.cos(self.x + self.t))
        self.line5.set_ydata(np.cosh(self.x + self.t))
        self.line6.set_ydata(np.tanh(self.x + self.t))
        self.line7.set_ydata(np.sin(self.x + self.t) * np.cos(self.x + self.t))
        self.line8.set_ydata(np.sin(self.x + self.t) + np.cos(self.x + self.t))
        
        self.ax[2].set_ylim(-10, 10)
        self.draw()
            
    