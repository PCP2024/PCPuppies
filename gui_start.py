import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QToolBar, QMessageBox, QWidget, QVBoxLayout, QFileDialog
)
from PyQt6.QtGui import QPixmap, QIcon, QAction, QImage
from PyQt6.QtCore import QSize, Qt
from processing import processing_fun
from PIL import Image, ImageFilter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PC Puppies - Image Processing GUI")

        self.current_pixmap = None
        self.original_pixmap = None  # for the original image
        self.max_width = 800  # maximum width for the image
        self.max_height = 600  # maximum height for image

        # Set up a button - example picture
        button = QPushButton("Example Picture")
        button.clicked.connect(self.button_click)

        self.setCentralWidget(button)

        # set up a toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(50, 50))
        self.addToolBar(toolbar)

        # set up a menu
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        # implement actions
        button_action_load = QAction(QIcon("load.jpg"), "Import image", self)
        button_action_load.triggered.connect(self.button_click_load)
        
        toolbar.addAction(button_action_load)
        file_menu.addAction(button_action_load)

        button_action_save = QAction(QIcon("icons/save-mini.jpg"), "Save image", self)
        button_action_save.triggered.connect(self.button_click_save)
        file_menu.addAction(button_action_save)
        
        button_action_mirror = QAction(QIcon("load.jpg"), "Mirror", self)
        button_action_mirror.triggered.connect(lambda: self.button_click_process(processing_fun.mirror))
        
        button_action_blur = QAction(QIcon("blur.jpg"), "Blur", self)
        button_action_blur.triggered.connect(lambda: self.button_click_process(processing_fun.blur))
        
        button_action_edge = QAction(QIcon("edge.jpg"), "Edge enhance", self)
        button_action_edge.triggered.connect(lambda: self.button_click_process(processing_fun.edge_enhance))

        button_action_edgef = QAction(QIcon("edgef.jpg"), "Find edges", self)
        button_action_edgef.triggered.connect(lambda: self.button_click_process(processing_fun.find_edges))

        button_action_smooth = QAction(QIcon("smooth.jpg"), "Smooth", self)
        button_action_smooth.triggered.connect(lambda: self.button_click_process(processing_fun.smooth))

        button_action_invert = QAction(QIcon("invert.jpg"), "Invert", self)
        button_action_invert.triggered.connect(lambda: self.button_click_process(processing_fun.invert))
        
        button_action_revert = QAction(QIcon("revert.jpg"), "Revert to Original", self)
        button_action_revert.triggered.connect(self.button_click_revert)
        toolbar.addAction(button_action_revert)

        file_menu = menu.addMenu("Processing")
        file_menu.addAction(button_action_blur)
        file_menu.addAction(button_action_mirror)
        file_menu.addAction(button_action_edge)
        file_menu.addAction(button_action_edgef)
        file_menu.addAction(button_action_smooth)
        file_menu.addAction(button_action_invert)
        file_menu.addAction(button_action_revert)

    def button_click(self):
        print("Button clicked - here is an example picture")
        self.display_image("demodata/PCPuppies_grouppicture.png")

    def display_image(self, image_path):
        label = QLabel(self)
        self.current_pixmap = QPixmap(image_path)
        self.original_pixmap = QPixmap(image_path)  # save the original image
        
        # Resize image to fit within the maximum dimensions
        self.current_pixmap = self.current_pixmap.scaled(self.max_width, self.max_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        
        label.setPixmap(self.current_pixmap)
        self.setCentralWidget(label)
        self.resize(self.current_pixmap.width(), self.current_pixmap.height())
        
    def button_click_process(self, process_function):
        if self.current_pixmap:
            image = self.current_pixmap.toImage()
            pil_image = Image.fromqpixmap(image)  # QImage to PIL Image

            altered_image = process_function(pil_image)

            altered_qimage = QImage(altered_image.tobytes(), altered_image.width, altered_image.height, QImage.Format.Format_RGB888)
            self.current_pixmap = QPixmap.fromImage(altered_qimage)  # altered image

            label = QLabel(self)
            label.setPixmap(self.current_pixmap)
            self.setCentralWidget(label)
            self.resize(self.current_pixmap.width(), self.current_pixmap.height())
        else:
            QMessageBox.warning(self, "No Image", "Please load an image first.")
            
    def button_click_load(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.jpg *.png *.jpeg)")
        if fileName:
            print("Loading file:", fileName)
            self.display_image(fileName)

    def button_click_save(self):
        if self.current_pixmap:
            fileName, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;JPG Files (*.jpg)")
            if fileName:
                self.current_pixmap.save(fileName)
                QMessageBox.information(self, "Image Saved", f"Image saved to: {fileName}")
            else:
                QMessageBox.warning(self, "Save Canceled", "The save operation was canceled.")
        else:
            QMessageBox.warning(self, "No Image", "No image to save.")
            
    def button_click_revert(self):
        if self.original_pixmap:
            label = QLabel(self)
            self.current_pixmap = self.original_pixmap  # Revert to the original image
            label.setPixmap(self.current_pixmap)
            self.setCentralWidget(label)
            self.resize(self.current_pixmap.width(), self.current_pixmap.height())
        else:
            QMessageBox.warning(self, "No Original Image", "No original image to revert to.")
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
