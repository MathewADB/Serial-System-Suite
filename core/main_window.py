from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt

from core.shortcuts import init_shortcuts
from ui.home import create_home_page
import serial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Serial System Suite")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        
        self.ser = serial.Serial()
        
        create_home_page(self)
        init_shortcuts(self)


