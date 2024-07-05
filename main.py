import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt

from gui.ui_main import Ui_MainWindow
from Views.View import View


class Application(QMainWindow, View):
    def __init__(self):
        super().__init__()
        self.initUi(self)
        self.set_connections()
        self.image = None
        self.modified_image = None

    def load_image(self):
        print("load image")
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.image = cv2.imread(file_name)
            if self.image is not None:
                self.modified_image = self.image.copy()
                self.display_image(self.image)
            else:
                QMessageBox.critical(self, "Error", "Failed to load image.")

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            QMessageBox.critical(self, 'Error', 'Failed to open webcam.')
            return
        ret, frame = cap.read()
        cap.release()
        if ret:
            self.image = frame
            self.modified_image = self.image.copy()
            self.display_image(self.image)
        else:
            QMessageBox.critical(self, 'Error', 'Failed to capture image.')

    def display_image(self, image):
        qformat = QImage.Format_RGB888 if len(image.shape) == 3 else QImage.Format_Indexed8
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w, ch = image.shape
        bytes_per_line = ch * w
        qimage = QImage(image.data, w, h, bytes_per_line, qformat)
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
