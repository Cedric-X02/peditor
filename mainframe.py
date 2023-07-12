from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)

        self.current_path = None
        self.current_fontsize = 8
        self.setWindowTitle("Untitled")

        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionSet_Dark_Mode.triggered.connect(self.setDarkMode)
        self.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.actionIncrease_Font_Size.triggered.connect(self.incFontSize)
        self.actionDecrease_Font_Size.triggered.connect(self.decFontSize)

    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None

    def saveFile(self):
        if self.current_path is not None:
            filetext = self.textEdit.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(filetext)
        else:
            self.saveFileAs

    def saveFileAs(self):
        fpath = QFileDialog.getSaveFileName(self, 'Save File', '%USERPROFILE%\Documents\\', 'Text files (*txt)')[0]
        fname = fpath.split("/")[-1]
        ftext = self.textEdit.toPlainText()
        with open(fpath, 'w') as f:
            f.write(ftext)
        self.current_path = fpath
        self.setWindowTitle(fname)

    def openFile(self):
        fpath = QFileDialog.getOpenFileName(self, 'Open File', '%USERPROFILE%\Documents\\', 'Text files (*txt)')[0]
        fname = fpath.split("/")[-1]
        self.setWindowTitle(fname)
        with open(fpath, 'r') as f:
            filetext = f.read()
            self.textEdit.setText(filetext)
        self.current_path = fpath

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def cut(self):
        self.textEdit.cut()

    def copy(self):
        self.textEdit.copy()

    def paste(self):
        self.textEdit.paste()

    def setDarkMode(self):
        self.setStyleSheet(
            'QWidget{background-color: rgb(33,33,33); color: #FFFFFF} QTextEdit{background-color: rgb(46,46,46)} QMenuBar::item:selected{color: #000000}'
        )
    
    def setLightMode(self):
        self.setStyleSheet('')

    def incFontSize(self):
        self.current_fontsize += 1
        self.textEdit.setFontPointSize(self.current_fontsize)

    def decFontSize(self):
        self.current_fontsize -= 1
        self.textEdit.setFontPointSize(self.current_fontsize)