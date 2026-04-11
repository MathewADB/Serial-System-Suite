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
        
        port_text = self.port_lbl.text()
        baud_text = self.baud_lbl.text()

        self.ser.port = port_text
        self.ser.baudrate = int(baud_text)

        self.ser.open()

    except Exception as e:
        self.err_box.setText(str(e))

def port_close(self):
    try:
        self.ser.close()
    except:
        pass