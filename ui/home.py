from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QTextEdit, QLineEdit, QPushButton)

from functools import partial
from ui.port_settings import PortSettingsDialog
from core.serial import port_open, port_close

def create_home_page(main_window):
    
    def update_labels(port, baud):
        main_window.port_lbl.setText(f"{port}")
        main_window.baud_lbl.setText(f"{baud}")
    
    def open_settings():
        dialog = PortSettingsDialog(main_window)
        dialog.settings_applied.connect(update_labels)
        dialog.exec()
        
    # ===== BASE WIDGET
    
    main_window.containerwidget = QWidget()
    main_window.containerwidget.setObjectName("XWidget")

    container_layout = QVBoxLayout(main_window.containerwidget)
    container_layout.setContentsMargins(0, 0, 0, 0) 
    container_layout.setSpacing(0)
    
    # ===== BUTTOM WIDGET
    
    setup_widget = QWidget()
    setup_widget.setObjectName("IWidget")
    setup_layout = QHBoxLayout(setup_widget)
    
    settingsButton = QPushButton("Port Settings")
    settingsButton.pressed.connect(open_settings)
    
    main_window.err_box = QLineEdit("Errors will be shown here")
    
    open_button = QPushButton("Open Port")
    open_button.pressed.connect(partial(port_open, main_window))
    
    close_button = QPushButton("Close Port")
    close_button.pressed.connect(partial(port_close, main_window))

    setup_layout.addWidget(settingsButton,1)
    setup_layout.addWidget(open_button,1)
    setup_layout.addWidget(close_button,1)
    setup_layout.addWidget(main_window.err_box,1)
    
    # ===== MID WIDGET
    
    terminal_widget = QWidget()
    terminal_widget.setObjectName("IWidget")
    terminal_layout = QHBoxLayout(terminal_widget)
    
    main_window.rx_box = QTextEdit()
    
    terminal_layout.addWidget(main_window.rx_box)
    
    # ===== TOP WIDGET
    
    info_widget = QWidget()
    info_widget.setObjectName("IWidget")
    info_layout = QHBoxLayout(info_widget)
    
    name_widget = QWidget()
    name_widget.setObjectName("IWidget")
    name_container = QVBoxLayout(name_widget)
    
    name_label = QLabel("Serial System Suite")
    version_label = QLabel("1.2.2")
    main_window.port_lbl = QLabel("None")
    main_window.baud_lbl = QLabel("56000")
    main_window.status_lbl = QLabel("Disconnected")
    
    name_container.addWidget(name_label)
    name_container.addWidget(version_label)
    
    connection_widget = QWidget()
    connection_widget.setObjectName("IWidget")
    connection_layout = QVBoxLayout(connection_widget)
    
    connection_layout.addWidget(main_window.port_lbl,1)
    connection_layout.addWidget(main_window.baud_lbl,1)
    connection_layout.addWidget(main_window.status_lbl,1)
    
    info_layout.addWidget(name_widget,1)
    info_layout.addWidget(QLabel(),2)
    info_layout.addWidget(connection_widget)
    
    # ===== FINALE
    
    container_layout.addWidget(info_widget,1)
    container_layout.addWidget(terminal_widget,8)
    container_layout.addWidget(setup_widget,1)        

    main_window.setCentralWidget(main_window.containerwidget)