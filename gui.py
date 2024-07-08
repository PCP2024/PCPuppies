import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QToolBar, QMessageBox, QWidget, QTextEdit, 
    QDialogButtonBox, QDialog, QVBoxLayout, QFileDialog, QLineEdit
)
from PyQt6.QtGui import QPixmap, QIcon, QAction, QImage
from PyQt6.QtCore import QSize, Qt
from processing import processing_fun
from analyze import analysis_fun
from PIL import Image, ImageFilter
from analyze import dogbreed_fun
import tempfile
import os

class AnalysisDialog(QDialog):
    def __init__(self, analysis_result, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Analysis Result")

        layout = QVBoxLayout()
        
        # text edit to show the analysis result
        result_text = QTextEdit()
        result_text.setReadOnly(True)
        result_text.setPlainText(analysis_result)
        layout.addWidget(result_text)

        self.setLayout(layout)
        self.setMinimumSize(400, 200)
                
class InputDialog(QDialog):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input Required")
        self.input_value = None

        layout = QVBoxLayout()

        self.label = QLabel(label_text)
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

    def accept(self):
        self.input_value = self.input_field.text()
        super().accept()

    def get_value(self):
        return self.input_value
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PC Puppies - Image Processing GUI")

        self.current_pixmap = None
        self.original_pixmap = None  # for the original image
        self.max_width = 800  # maximum width for the image
        self.max_height = 600  # maximum height for image
        self.history_stack = []
        
        # Set up a button - example picture
        button = QPushButton("Example Picture")
        button.clicked.connect(self.button_click)

        self.setCentralWidget(button)

        # set up a toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)

        # set up a menu
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        # implement actions
        button_action_load = QAction(QIcon("icons/import.png"), "Import image", self)
        button_action_load.triggered.connect(self.button_click_load)
        
        #toolbar.addAction(button_action_load)
        file_menu.addAction(button_action_load)

        button_action_save = QAction(QIcon("icons/save.png"), "Save image", self)
        button_action_save.triggered.connect(self.button_click_save)
        file_menu.addAction(button_action_save)
        
        button_action_rotate = QAction(QIcon("icons/rotate.png"), "Rotate", self)
        button_action_rotate.triggered.connect(lambda: self.button_click_with_input("Enter degree of rotation:", processing_fun.rotate))
        
        button_action_mirror = QAction(QIcon("icons/mirror.png"), "Mirror", self)
        button_action_mirror.triggered.connect(lambda: self.button_click_process(processing_fun.mirror))
        
        button_action_blur = QAction(QIcon("icons/cute_humans.png"), "Blur", self)
        button_action_blur.triggered.connect(lambda: self.button_click_process(processing_fun.blur))
        
        button_action_edge = QAction(QIcon("icons/edge_enhance.png"), "Edge enhance", self)
        button_action_edge.triggered.connect(lambda: self.button_click_process(processing_fun.edge_enhance))

        button_action_edgef = QAction(QIcon("icons/find_edges.png"), "Find edges", self)
        button_action_edgef.triggered.connect(lambda: self.button_click_process(processing_fun.find_edges))

        button_action_smooth = QAction(QIcon("icons/smooth.png"), "Smooth", self)
        button_action_smooth.triggered.connect(lambda: self.button_click_process(processing_fun.smooth))

        button_action_invert = QAction(QIcon("icons/invert.png"), "Invert", self)
        button_action_invert.triggered.connect(lambda: self.button_click_process(processing_fun.invert))
        
        button_action_thresh = QAction(QIcon("icons/thresh.png"), "Apply threshold", self)
        button_action_thresh.triggered.connect(lambda: self.button_click_with_input("Enter threshold:", processing_fun.apply_threshold))
        
        
        button_action_toNumpyArray = QAction(QIcon("icons/numpy.jpg"), "Convert to numpy Array", self)
        button_action_toNumpyArray.triggered.connect(lambda: self.button_click_analysis(analysis_fun.imageToNumpyArray))
        
        button_action_shape = QAction(QIcon("icons/shape.png"), "Get shape", self)
        button_action_shape.triggered.connect(lambda: self.button_click_analysis(analysis_fun.get_image_shape))
        
        button_action_undo = QAction(QIcon("icons/undo.png"), "Undo", self)
        button_action_undo.triggered.connect(self.button_click_undo)
        toolbar.addAction(button_action_undo)
        
        button_action_revert = QAction(QIcon("icons/original.png"), "Original image", self)
        button_action_revert.triggered.connect(self.button_click_revert)
        toolbar.addAction(button_action_revert)
        
        button_action_classify = QAction(QIcon("icons/classifier.png"), "Classify Dog Breed", self)
        button_action_classify.triggered.connect(self.classify_dog_breed)
        
        file_menu = menu.addMenu("Processing")
        file_menu.addAction(button_action_rotate)
        file_menu.addAction(button_action_blur)
        file_menu.addAction(button_action_mirror)
        file_menu.addAction(button_action_edge)
        file_menu.addAction(button_action_edgef)
        file_menu.addAction(button_action_smooth)
        file_menu.addAction(button_action_invert)
        file_menu.addAction(button_action_thresh)
        
        file_menu = menu.addMenu("Analysis")
        file_menu.addAction(button_action_toNumpyArray)
        file_menu.addAction(button_action_shape)
    
        file_menu = menu.addMenu("What Breed Am I?")
        file_menu.addAction(button_action_classify)

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
            # Save the current state to the history stack before processing
            self.history_stack.append(self.current_pixmap.copy())
            
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
    
    def button_click_analysis(self, analysis_function):
        if self.current_pixmap:
            image = self.current_pixmap.toImage()
            pil_image = Image.fromqpixmap(image)  # QImage to PIL Image

            altered_image = analysis_function(pil_image)

            analysis_result = str(altered_image)

            dialog = AnalysisDialog(analysis_result, self)
            dialog.exec()
        else:
            QMessageBox.warning(self, "No Image", "Please load an image first.")

    def classify_dog_breed(self):
        if self.current_pixmap:
            image = self.current_pixmap.toImage()
            pil_image = Image.fromqpixmap(image)  # QImage to PIL Image

            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                pil_image.save(temp_file, format='JPEG')
                temp_file_path = temp_file.name
            
            # classification 
            breed = dogbreed_fun.classify_dogbreed(temp_file_path)
            analysis_result = str(breed[0]) 
            # clean up the temporary file
            os.remove(temp_file_path)
            
            dialog = AnalysisDialog(analysis_result, self)
            dialog.exec()
        else:
            QMessageBox.warning(self, "No Image", "Please load an image first.")     
        
    def button_click_with_input(self, label_text, process_function):
        if self.current_pixmap:
            dialog = InputDialog(label_text, self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                input_value = dialog.get_value()
                try:
                    input_value = float(input_value)
                    self.button_click_process(lambda img: process_function(img, input_value))
                except ValueError:
                    QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
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
    
    def button_click_undo(self):
        if self.history_stack:
            self.current_pixmap = self.history_stack.pop()

            label = QLabel(self)
            label.setPixmap(self.current_pixmap)
            self.setCentralWidget(label)
            self.resize(self.current_pixmap.width(), self.current_pixmap.height())
        else:
            QMessageBox.warning(self, "No History", "No previous state to revert to.")
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
