from PyQt6.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QTextEdit, QLineEdit)
from PyQt6.QtCore import Qt

from core.shortcuts import init_shortcuts

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Serial System Suite")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        
        self.containerwidget = QWidget()
        self.containerwidget.setObjectName("XWidget")

        container_layout = QVBoxLayout(self.containerwidget)
        container_layout.setContentsMargins(0, 0, 0, 0) 
        container_layout.setSpacing(0)
        
        setup_widget = QWidget()
        setup_widget.setObjectName("IWidget")
        setup_layout = QHBoxLayout(setup_widget)
        
        self.port_box = QComboBox()
        self.buad_box = QComboBox()
        self.status_label = QLineEdit("Errors will be shown here")
        
        setup_layout.addWidget(self.port_box,1)
        setup_layout.addWidget(self.buad_box,1)
        setup_layout.addWidget(self.status_label,1)
        
        terminal_widget = QWidget()
        terminal_widget.setObjectName("IWidget")
        terminal_layout = QHBoxLayout(terminal_widget)
        
        self.terminal_box = QTextEdit()
        
        terminal_layout.addWidget(self.terminal_box)
        
        info_widget = QWidget()
        info_widget.setObjectName("IWidget")
        info_layout = QHBoxLayout(info_widget)
        
        name_label = QLabel("Serial System Suite")
        version_label = QLabel("1.0.1")
        device_label = QLabel("Null")
        status_label = QLabel("Disconnected")
        
        info_layout.addWidget(name_label)
        info_layout.addWidget(version_label)
        info_layout.addWidget(device_label)
        info_layout.addWidget(status_label)
                
        container_layout.addWidget(info_widget,1)
        container_layout.addWidget(terminal_widget,8)
        container_layout.addWidget(setup_widget,1)        

        self.setCentralWidget(self.containerwidget)
        
        self.setCentralWidget(self.containerwidget)
        
        init_shortcuts(self)
        

