#Main program to test funtions
import sys, os.path
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog, QColorDialog, QLabel
from PyQt5.QtGui import QColor, QIcon, QTextCursor
from PyQt5.QtCore import Qt, pyqtSlot

class mainWindow(QMainWindow):
    #Constructer
    def __init__(self):
        super().__init__()
        self.iniUI()
    
    def iniUI(self):
        '''
        Initialize the window and display contents to the screen
        '''
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('DCR Toolware')
        self.setWindowIcon(QIcon('./image/ava_Ucap.png'))
        # self.dcrWidget()
        self.dcrMenu()
        self.mainWidget()
        self.show()

    # def dcrWidget(self):
    #     '''
    #     Set the widget for mainWindow
    #     '''
    def dcrMenu(self):
        '''
        Create menu with the scratch funtions
        Action for file menu 
        '''
        open_act = QAction(QIcon('./image/open.png'), 'Open ...', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.openFile)

        export_act = QAction(QIcon('./image/export.png'), 'Export', self)
        export_act.setShortcut('Ctrl+K')
        #export_act.triggered.connect(self.exportFile)

        save_act = QAction(QIcon('./image/save.png'), 'Save', self)
        save_act.setShortcut('Ctrl+S')
        #save_act.triggered.connect(self.exportFile)

        #Create menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        #Create file menu and add Action 
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(open_act)
        # file_menu.addSeparator()
        file_menu.addAction(export_act)
        file_menu.addSeparator()
        file_menu.addAction(save_act)
        
    def mainWidget(self):
        QLabel("Choosen File", self).move(10, 50)
        name_label = QLabel("dir/file :", self)
        name_label.move(10, 70)



    def openFile(self):
        '''
        Choose the file we want to filter
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", 
                                                        "/home", 
                                                        "ALL")
        print(file_name)
        '''
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        print(dir_)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())

