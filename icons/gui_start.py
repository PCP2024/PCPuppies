import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QLabel, QToolBar



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PC Puppies")

        button = QPushButton("Click me")
        button.clicked.connect(self.button_click)

        self.setCentralWidget(button)

    def button_click(self):
        print("Button clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()