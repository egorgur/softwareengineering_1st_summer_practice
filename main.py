import os.path
import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtGui import QImage, QPixmap, QDesktopServices
from PySide6.QtCore import Qt, QUrl

from gui.ui_main import Ui_MainWindow
from Views.View import View


class Application(QMainWindow, View):
    def __init__(self):
        super().__init__()
        self.initUi(self)
        self.set_connections()
        self.image = None
        self.modified_image = None
        self.rgb_channels_modified_image = None

    def load_image(self):
        print("load image")
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.image = cv2.imread(file_name)
            if self.image is not None:
                self.modified_image = self.image.copy()
                self.rgb_channels_modified_image = self.image.copy()
                self.rotate_angle_spinbox.setValue(0)
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
            self.rgb_channels_modified_image = self.image.copy()
            self.rotate_angle_spinbox.setValue(0)
            self.display_image(self.image)
        else:
            QMessageBox.critical(self, 'Error', 'Failed to capture image.')

    def display_image(self, image):
        if image is not None:
            qformat = QImage.Format_RGB888 if len(image.shape) == 3 else QImage.Format_Indexed8
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, ch = image.shape
            bytes_per_line = ch * w
            qimage = QImage(image.data, w, h, bytes_per_line, qformat)
            pixmap = (QPixmap.fromImage(qimage)
                      .scaled(self.image_display_label.size(), aspectMode=Qt.AspectRatioMode.KeepAspectRatio))
            self.image_display_label.setPixmap(pixmap)
            self.image_display_label.repaint()

    def show_channels(self):
        """
        Takes the state of the menu bar channels boolean values
        and displays the modified image without modifying the source image
        :return:
        """
        if self.image is None:
            QMessageBox.critical(self, 'Error', 'No image loaded')
            return None

        red_mask: bool = self.red_channel_action.isChecked()
        green_mask: bool = self.green_channel_action.isChecked()
        blue_mask: bool = self.blue_channel_action.isChecked()

        image = self.modified_image.copy()

        if not red_mask:
            image[:, :, 2] = 0
        if not green_mask:
            image[:, :, 1] = 0
        if not blue_mask:
            image[:, :, 0] = 0

        self.rgb_channels_modified_image = image

        self.display_image(image)

    def show_negative(self):
        if self.image is None:
            QMessageBox.warning(self, "Warning", "No image loaded")
            return

        # return the state of the channels checkboxes for consistency
        self.red_channel_action.setChecked(True)
        self.green_channel_action.setChecked(True)
        self.blue_channel_action.setChecked(True)

        if self.negative_action.isChecked():
            negative_image = cv2.bitwise_not(self.modified_image)
            self.modified_image = negative_image
            self.display_image(negative_image)
        else:
            negative_image = cv2.bitwise_not(self.modified_image)
            self.modified_image = negative_image
            self.display_image(negative_image)
        self.rgb_channels_modified_image = self.modified_image.copy()

    def increase_current_rotation_angle_by_5_right(self):
        if self.image is None:
            return

        self.rotate_angle_spinbox.setValue(self.rotate_angle_spinbox.value() - 5)
        self.rotate_image()

    def increase_current_rotation_angle_by_5_left(self):
        if self.image is None:
            return

        self.rotate_angle_spinbox.setValue(self.rotate_angle_spinbox.value() + 5)
        self.rotate_image()

    def rotate_image(self):
        if self.image is None:
            return

        angle = self.rotate_angle_spinbox.value()
        (h, w) = self.image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(self.modified_image, M, (w, h))
        self.display_image(rotated)

    def draw_circle(self):
        if self.image is None:
            QMessageBox.warning(self, "Warning", "No image loaded.")
            return

        x, ok = QInputDialog.getInt(self, "Input", "Enter x coordinate:")
        if not ok:
            return
        y, ok = QInputDialog.getInt(self, "Input", "Enter y coordinate:")
        if not ok:
            return
        radius, ok = QInputDialog.getInt(self, "Input", "Enter radius:")
        if not ok:
            return

        circle_image = self.modified_image.copy()
        (h, w) = self.image.shape[:2]
        cv2.circle(circle_image, (x, h - y), radius, (0, 0, 255), 2)
        self.modified_image = circle_image.copy()
        self.display_image(circle_image)

    def get_filtered_image(self):
        self.show_channels()
        return self.rgb_channels_modified_image


    # def save_image(self):
    #     if self.modified_image is None:
    #         QMessageBox.warning(self, "Warning", "No image to save.")
    #         return
    #     if self.image is None:
    #         QMessageBox.warning(self, "Warning", "No image to save.")
    #         return
    #
    #     file_name, _ = QFileDialog.getSaveFileName(self, "Save Image File", "",
    #                                                "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)")
    #     file_name: str
    #     print(os.path.join(file_name.split("/")))
    #     print(file_name)
    #     if file_name:
    #         success = cv2.imwrite(file_name, self.get_filtered_image())
    #         print(success)
    #         if success:
    #             QMessageBox.information(self, "Success", f"Image saved to {file_name}")
    #         else:
    #             QMessageBox.critical(self, "Error", "Failed to save image.")

    def github_redirect(self):
        url = QUrl("https://github.com/egorgur/softwareengineering_1st_summer_practice")
        QDesktopServices.openUrl(url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
