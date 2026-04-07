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
        #self.set_on_off(True)
    except Exception as e:
        self.err_box.append(str(e))

def port_close(self):
    try:
        self.ser.close()
        #self.set_on_off(False)
    except:
        pass