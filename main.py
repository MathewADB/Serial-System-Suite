import sys

from PyQt6.QtWidgets import QApplication
#from PyQt6 import QtGui

from core.main_window import MainWindow
from tools.styles import load_styles

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    #window.setWindowIcon(QtGui.QIcon('data\\icon.ico'))

    load_styles(app)
    window.show()
    sys.exit(app.exec())