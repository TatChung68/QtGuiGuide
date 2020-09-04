# dialogs.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton)
from PyQt5.QtGui import QFont
class DisplayMessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() # Call our function used to set up window
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QMessageBox Example')
        self.displayWidgets()
        self.show()
    def displayWidgets(self):
        """
        Set up the widgets.
        """
        catalogue_label = QLabel("Author Catalogue", self)
        catalogue_label.move(20, 20)
        catalogue_label.setFont(QFont('Arial', 20))
        auth_label = QLabel("Enter the name of the author you are searchingfor:", self)
        auth_label.move(40, 60)
        # Create author label and line edit widgets
        author_name = QLabel("Name:", self)
        author_name.move(50, 90)
        self.auth_entry = QLineEdit(self)
        self.auth_entry.move(95, 90)
        self.auth_entry.resize(240, 20)
        self.auth_entry.setPlaceholderText("firstname lastname")
        # Create search button
        search_button = QPushButton("Search", self)
        search_button.move(125, 130)
        search_button.resize(150, 40)
        search_button.clicked.connect(self.displayMessageBox)
    def displayMessageBox(self):
        """
        When button is clicked, search through catalogue of names.
        If name is found, display Author Found dialog.
        Otherwise, display Author Not Found dialog.
        """
        # Check if authors.txt exists
        # try:
        #     with open("files/authors.txt", "r") as f:
        #         # read each line into a list
        #         authors = [line.rstrip('\n') for line in f]
        # except FileNotFoundError:
        #     print("The file cannot be found.")
        # Check for name in list
        not_found_msg = QMessageBox() # create not_found_msg object to avoid causing a 'referenced before assignment' error
        if self.auth_entry.text() == 'Nam':
            QMessageBox().information(self, self.auth_entry.text(), "Love You", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            not_found_msg = QMessageBox.question(self, "Author Not Found", "Author notauth_entry.text() found izn catalogue.\nDo you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if not_found_msg == QMessageBox.No:
            print("Closing application.")
            self.close()
        else:
            pass
# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayMessageBox()
    sys.exit(app.exec_())