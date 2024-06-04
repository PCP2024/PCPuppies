import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QToolBar, QWidget, QVBoxLayout, QFileDialog
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import QSize


# class AnotherWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()


   



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
        button_action_save = QAction(QIcon("demodata\example_pic.jpg"), "Save", self) 
        button_action_load.triggered.connect(self.ButtonClickLoad)
        toolbar.addAction(button_action_load)

        # set up a menu
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action_load)          
        file_menu.addAction(button_action_save)

        button_action_blur = QAction("Apply Blurring", self)
        button_action_blur.setStatusTip("Apply a blurring effect to the image")
        button_action_blur.triggered.connect(self.button_click_blur)

        file_menu = menu.addMenu("Processing")
        file_menu.addAction(button_action_blur)




    def button_click(self):
        print("Button clicked")

    def button_click_pic(self):
        label = QLabel(self)
        pixmap = QPixmap("demodata\PCPuppies_grouppicture.png")
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    def button_click_blur(self):
        label = QLabel(self)
        pixmap = QPixmap("demodata\PCPuppies_grouppicture.png")
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    # def open new window(): # for user to specify the parameters/configurations

    def ButtonClickLoad(self, s):
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "JPG files (*.jpg);; PNG files (*.png)") 
        if fileName:
            print("loading file: ", fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()