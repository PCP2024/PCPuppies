import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QToolBar
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PC Puppies")

        # Set up a button
        button = QPushButton("Click me")
        button.clicked.connect(self.button_click)

        self.setCentralWidget(button)

        # Set up a toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(50, 50))
        self.addToolBar(toolbar)

        button_action_load = QAction(QIcon("demodata\example_pic.jpg"), "Click me", self)
        button_action_load.triggered.connect(self.button_click_pic)
        toolbar.addAction(button_action_load)


    def button_click(self):
        print("Button clicked")

    def button_click_pic(self):
        label = QLabel(self)
        pixmap = QPixmap("demodata\PCPuppies_grouppicture.png")
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()