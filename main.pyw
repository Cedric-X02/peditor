import mainframe, sys, requests
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":

    r = requests.get()

    app = QApplication(sys.argv)
    ui = mainframe.Main()
    ui.show()
    app.exec_()