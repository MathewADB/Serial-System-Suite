import serial
import serial.tools.list_ports
        
def refresh_ports(self):
    self.port_box.clear()
    ports = serial.tools.list_ports.comports()
    for p in ports:
        self.port_box.addItem(p.device)
    
def port_open(self):
    try:
        self.ser.close()
        self.ser.port = self.port_box.currentText()
        self.ser.baudrate = int(self.baud_box.currentText())
        self.ser.open()
        self.status_label.setText("Connected")
    except Exception as e:
        self.err_box.setText(str(e))

def port_close(self):
    try:
        self.ser.close()
        self.status_label.setText("Disconnected")
    except:
        pass