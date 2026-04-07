from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QTextEdit, QLineEdit, QPushButton)

from core.serial import refresh_ports,port_open,port_close
from functools import partial

def create_home_page(main_window):
    
    main_window.containerwidget = QWidget()
    main_window.containerwidget.setObjectName("XWidget")

    container_layout = QVBoxLayout(main_window.containerwidget)
    container_layout.setContentsMargins(0, 0, 0, 0) 
    container_layout.setSpacing(0)
    
    setup_widget = QWidget()
    setup_widget.setObjectName("IWidget")
    setup_layout = QHBoxLayout(setup_widget)
    
    main_window.port_box = QComboBox()
    refresh_ports(main_window)
        
    main_window.baud_box = QComboBox()
    
    main_window.baud_box.addItems([
        "110","300","600","1200","2400","4800","9600",
        "19200","38400","57600","115200","230400"
    ])
    main_window.baud_box.setCurrentText("57600")
    
    main_window.err_box = QTextEdit("Errors will be shown here")
    
    open_button = QPushButton("Open Port")
    open_button.pressed.connect(partial(port_open, main_window))
    
    close_button = QPushButton("Close Port")
    close_button.pressed.connect(partial(port_close, main_window))

    setup_layout.addWidget(main_window.port_box,1)
    setup_layout.addWidget(main_window.baud_box,1)
    setup_layout.addWidget(open_button,1)
    setup_layout.addWidget(close_button,1)
    setup_layout.addWidget(main_window.err_box,1)
    
    terminal_widget = QWidget()
    terminal_widget.setObjectName("IWidget")
    terminal_layout = QHBoxLayout(terminal_widget)
    
    main_window.terminal_box = QTextEdit()
    
    terminal_layout.addWidget(main_window.terminal_box)
    
    info_widget = QWidget()
    info_widget.setObjectName("IWidget")
    info_layout = QHBoxLayout(info_widget)
    
    name_widget = QWidget()
    name_widget.setObjectName("IWidget")
    name_container = QVBoxLayout(name_widget)
    name_label = QLabel("Serial System Suite")
    
    version_label = QLabel("1.1.2")
    device_label = QLabel("Null")
    status_label = QLabel("Disconnected")
    
    name_container.addWidget(name_label)
    name_container.addWidget(version_label)
    
    info_layout.addWidget(name_widget)
    info_layout.addWidget(device_label)
    info_layout.addWidget(status_label)
            
    container_layout.addWidget(info_widget,1)
    container_layout.addWidget(terminal_widget,8)
    container_layout.addWidget(setup_widget,1)        

    main_window.setCentralWidget(main_window.containerwidget)
    
    main_window.setCentralWidget(main_window.containerwidget)