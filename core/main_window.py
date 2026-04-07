from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt

from core.shortcuts import init_shortcuts
from core.serial import refresh_ports
from ui.home import create_home_page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Serial System Suite")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        
        create_home_page(self)
        init_shortcuts(self)
        refresh_ports(self)

