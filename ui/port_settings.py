from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton,
    QComboBox, QHBoxLayout)

from functools import partial
from core.serial import refresh_ports

class PortSettingsDialog(QDialog):
    settings_applied = pyqtSignal(str, str)  
    def __init__(self, port_service):
        super().__init__()

        self.port_service = port_service
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.setWindowTitle("Port Settings")
        
        layout = QVBoxLayout()
        
        self.port_box = QComboBox()
        refresh_ports(self)
            
        self.baud_box = QComboBox()
        self.baud_box.addItems([
            "110","300","600","1200","2400","4800","9600",
            "19200","38400","57600","115200","230400"])
        self.baud_box.setCurrentText("57600")
        
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(partial(refresh_ports, self))
        
        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(self.apply_and_close)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        
        layout.addWidget(QLabel("Port Settings"))

        layout.addWidget(self.port_box)
        layout.addWidget(self.baud_box)
        layout.addWidget(refresh_btn)
        layout.addWidget(apply_btn)
        layout.addWidget(close_btn)
        
        self.setLayout(layout)
    
    def apply_and_close(self):
        port = self.port_box.currentText()
        baud = self.baud_box.currentText()
    
        self.settings_applied.emit(port, baud)
        self.close()