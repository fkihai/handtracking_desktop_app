import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # QLabel untuk menampilkan plot
        self.label = QLabel(self)
        layout.addWidget(self.label)

        self.plot_graph()  # Panggil fungsi untuk menampilkan plot

    def plot_graph(self):
        # Buat figure Matplotlib
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Buat data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plot grafik
        ax.plot(x, y, label="Sine Wave")
        ax.set_title("Grafik Sinus")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.legend()

        # Render grafik ke gambar
        canvas.draw()
        width, height = fig.canvas.get_width_height()
        image = np.frombuffer(canvas.buffer_rgba(), dtype=np.uint8).reshape(height, width, 4)

        # Konversi ke QPixmap
        qimage = QImage(image, width, height, QImage.Format.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)
        
        return pixmap

        # Tampilkan di QLabel
