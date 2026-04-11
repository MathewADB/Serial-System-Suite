import serial
import serial.tools.list_ports
from PyQt6.QtCore import QTimer

def refresh_ports(self):
    self.port_box.clear()
    ports = serial.tools.list_ports.comports()
    for p in ports:
        self.port_box.addItem(p.device)
    
def port_open(self):
    try:
        if self.ser.is_open:
            self.ser.close()
        
        port_text = self.port_lbl.text()
        baud_text = self.baud_lbl.text()

        
        self.ser.port = port_text
        self.ser.baudrate = int(baud_text)

        self.ser.open()
        self.status_lbl.setText("Connected")

    except Exception as e:
        self.err_box.setText(str(e))

def port_close(self):
    try:
        self.ser.close()
        self.status_lbl.setText("Disconnected")
    except:
        pass
    
def receive_data(self):
    if not self.ser.is_open:
        return

    try:
        if not self.ser.in_waiting:
            return
        raw_data = self.ser.read(self.ser.in_waiting)
        
    except Exception as e:
        self.err_box.setText(str(e))
        return

    decoded = list(raw_data)

    self.rx_box.append(str(decoded))