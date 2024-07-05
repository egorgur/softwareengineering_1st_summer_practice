from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QFrame, QHBoxLayout, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QSpacerItem, QSpinBox, QVBoxLayout, QWidget)


class View():
    def initUi(self, MainWindow: QMainWindow):
        MainWindow.setWindowTitle("Image Redactor")

        # transformed from .ui file
        MainWindow.resize(900, 800)
        MainWindow.setMinimumSize(QSize(500, 300))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.choose_file_action = QAction(MainWindow)
        self.choose_file_action.setObjectName(u"choose_file_action")
        self.save_action = QAction(MainWindow)
        self.save_action.setObjectName(u"save_action")
        self.actionTrsfewfwefwe = QAction(MainWindow)
        self.actionTrsfewfwefwe.setObjectName(u"actionTrsfewfwefwe")
        self.actionerfgwergewrg = QAction(MainWindow)
        self.actionerfgwergewrg.setObjectName(u"actionerfgwergewrg")
        self.actionerfgwergewrg.setEnabled(True)
        self.actionwegfwegwreg = QAction(MainWindow)
        self.actionwegfwegwreg.setObjectName(u"actionwegfwegwreg")
        self.negative_action = QAction(MainWindow)
        self.negative_action.setObjectName(u"negative_action")
        self.negative_action.setCheckable(True)
        self.red_channel_action = QAction(MainWindow)
        self.red_channel_action.setObjectName(u"red_channel_action")
        self.red_channel_action.setCheckable(True)
        self.red_channel_action.setChecked(True)
        self.green_channel_action = QAction(MainWindow)
        self.green_channel_action.setObjectName(u"green_channel_action")
        self.green_channel_action.setCheckable(True)
        self.green_channel_action.setChecked(True)
        self.blue_channel_action = QAction(MainWindow)
        self.blue_channel_action.setObjectName(u"blue_channel_action")
        self.blue_channel_action.setCheckable(True)
        self.blue_channel_action.setChecked(True)
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.vebcam_capture_action = QAction(MainWindow)
        self.vebcam_capture_action.setObjectName(u"vebcam_capture_action")
        self.about_action = QAction(MainWindow)
        self.about_action.setObjectName(u"about_action")
        icon = QIcon()
        icon.addFile(u"img/github_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_action.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border: 1px solid #4d4e51;\n"
                                         "background-color: #1e1f22;"
                                         "color: #d1d1cc;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.inner_frame = QFrame(self.centralwidget)
        self.inner_frame.setObjectName(u"inner_frame")
        self.inner_frame.setEnabled(True)
        self.inner_frame.setStyleSheet(u"QPushButton:hover{\n"
                                       "color: white;\n"
                                       "}")
        self.inner_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.inner_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.inner_frame)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 25))
        self.header_widget.setMaximumSize(QSize(16777215, 25))
        self.header_widget.setStyleSheet(u"padding: 0 5px 0 5px;\n"
                                         "")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 0, 4, 0)
        self.turl_left_5_btn = QPushButton(self.header_widget)
        self.turl_left_5_btn.setObjectName(u"turl_left_5_btn")
        self.turl_left_5_btn.setMinimumSize(QSize(20, 0))
        self.turl_left_5_btn.setMaximumSize(QSize(20, 20))
        self.turl_left_5_btn.setStyleSheet(u"QWidget {\n"
                                           "padding: 0;\n"
                                           "margin: 1px;\n"
                                           "}")

        self.horizontalLayout_2.addWidget(self.turl_left_5_btn)

        self.turn_right_5_btn = QPushButton(self.header_widget)
        self.turn_right_5_btn.setObjectName(u"turn_right_5_btn")
        self.turn_right_5_btn.setMinimumSize(QSize(20, 0))
        self.turn_right_5_btn.setStyleSheet(u"QWidget {\n"
                                            "padding: 0;\n"
                                            "margin: 1px;\n"
                                            "}")

        self.horizontalLayout_2.addWidget(self.turn_right_5_btn)

        self.rotate_angle_spinbox = QSpinBox(self.header_widget)
        self.rotate_angle_spinbox.setObjectName(u"rotate_angle_spinbox")
        self.rotate_angle_spinbox.setStyleSheet(u"color: white;\n"
                                                "")
        self.rotate_angle_spinbox.setMinimum(-360)
        self.rotate_angle_spinbox.setMaximum(360)

        self.horizontalLayout_2.addWidget(self.rotate_angle_spinbox)

        self.horizontalSpacer = QSpacerItem(872, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addWidget(self.header_widget)

        self.main_space_widget = QWidget(self.inner_frame)
        self.main_space_widget.setObjectName(u"main_space_widget")
        self.horizontalLayout = QHBoxLayout(self.main_space_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.panel_left_widget = QWidget(self.main_space_widget)
        self.panel_left_widget.setObjectName(u"panel_left_widget")
        self.panel_left_widget.setMinimumSize(QSize(125, 0))
        self.panel_left_widget.setMaximumSize(QSize(125, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.panel_left_widget)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.draw_circle_instr = QPushButton(self.panel_left_widget)
        self.draw_circle_instr.setObjectName(u"draw_circle_instr")
        self.draw_circle_instr.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.draw_circle_instr)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.panel_left_widget)

        self.work_space_frame = QFrame(self.main_space_widget)
        self.work_space_frame.setObjectName(u"work_space_frame")
        self.work_space_frame.setMouseTracking(True)
        self.work_space_frame.setStyleSheet(u"QWidget {\n"
                                            "padding: 0;\n"
                                            "margin: 1px;\n"
                                            "}")
        self.work_space_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.work_space_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.image_display_label = QLabel(self.work_space_frame)
        self.image_display_label.setObjectName(u"image_display_label")
        self.image_display_label.setStyleSheet(u"margin: 10px;")
        self.image_display_label.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.image_display_label)

        self.horizontalLayout.addWidget(self.work_space_frame)

        self.panel_right_widget = QWidget(self.main_space_widget)
        self.panel_right_widget.setObjectName(u"panel_right_widget")
        self.panel_right_widget.setMinimumSize(QSize(125, 0))
        self.panel_right_widget.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout.addWidget(self.panel_right_widget)

        self.verticalLayout_2.addWidget(self.main_space_widget)

        self.footer_widget = QWidget(self.inner_frame)
        self.footer_widget.setObjectName(u"footer_widget")
        self.footer_widget.setMinimumSize(QSize(25, 25))
        self.footer_widget.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.footer_widget)

        self.verticalLayout.addWidget(self.inner_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 986, 22))
        self.menuBar.setStyleSheet(u"QMenuBar{\n"
                                   "background-color:#2b2d30;\n"
                                   "color: #d1d1cc;\n"
                                   "}\n"
                                   "QMenuBar::item:selected{\n"
                                   "color: #e2e2dd;\n"
                                   "background: #4d4e51;\n"
                                   "}\n"
                                   "QMenu{\n"
                                   "background-color:#2b2d30;\n"
                                   "color: #d1d1cc;\n"
                                   "border: 1px solid #18191c;\n"
                                   "}\n"
                                   "QMenu::item{\n"
                                   "background-color:#2b2d30;\n"
                                   "color: #d1d1cc;\n"
                                   "margin: 0;\n"
                                   "padding: 2px 8px 2px 4px;\n"
                                   "}\n"
                                   "QMenu::item:selected{\n"
                                   "color: #e2e2dd;\n"
                                   "background: #4d4e51;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "r")
        self.file_menu = QMenu(self.menuBar)
        self.file_menu.setObjectName(u"file_menu")
        self.edit_menu = QMenu(self.menuBar)
        self.edit_menu.setObjectName(u"edit_menu")
        self.channels_menu = QMenu(self.edit_menu)
        self.channels_menu.setObjectName(u"channels_menu")
        self.help_menu = QMenu(self.menuBar)
        self.help_menu.setObjectName(u"help_menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.file_menu.menuAction())
        self.menuBar.addAction(self.edit_menu.menuAction())
        self.menuBar.addAction(self.help_menu.menuAction())
        self.file_menu.addAction(self.choose_file_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.vebcam_capture_action)
        self.edit_menu.addAction(self.channels_menu.menuAction())
        self.edit_menu.addAction(self.negative_action)
        self.channels_menu.addAction(self.red_channel_action)
        self.channels_menu.addAction(self.green_channel_action)
        self.channels_menu.addAction(self.blue_channel_action)
        self.help_menu.addAction(self.about_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choose_file_action.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b...",
                                                                   None))
        self.save_action.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.actionTrsfewfwefwe.setText(QCoreApplication.translate("MainWindow", u"Trsfewfwefwe", None))
        self.actionerfgwergewrg.setText(QCoreApplication.translate("MainWindow", u"erfgwergewrg", None))
        self.actionwegfwegwreg.setText(QCoreApplication.translate("MainWindow", u"wegfwegwreg", None))
        self.negative_action.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0433\u0430\u0442\u0438\u0432", None))
        self.red_channel_action.setText(
            QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.green_channel_action.setText(
            QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b\u0451\u043d\u044b\u0439", None))
        self.blue_channel_action.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u043f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u043b\u0435\u0432\u043e (5 \u0433\u0440\u0430\u0434\u0443\u0441\u043e\u0432)",
                                                         None))
        self.action_6.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u043f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u043f\u0440\u0430\u0432\u043e (5 \u0433\u0440\u0430\u0434\u0443\u0441\u043e\u0432)",
                                                         None))
        self.vebcam_capture_action.setText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0421\u043d\u044f\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441 \u043a\u0430\u043c\u0435\u0440\u044b",
                                                                      None))
        self.about_action.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435...",
                                                             None))
        self.turl_left_5_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.turn_right_5_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.rotate_angle_spinbox.setSuffix(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.draw_circle_instr.setText(QCoreApplication.translate("MainWindow", u"Draw Sircle", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.edit_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.channels_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b\u044b", None))
        self.help_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))

    # retranslateUi

    def set_connections(self):
        """
        Bind the callback funcs of the App to ui interactive elements
        :return:
        """
        self.choose_file_action.triggered.connect(self.load_image)

        # Tries to capture an image from the vebcamera
        self.vebcam_capture_action.triggered.connect(self.capture_image)

        # RGB channels connections
        self.red_channel_action.triggered.connect(self.show_channels)
        self.green_channel_action.triggered.connect(self.show_channels)
        self.blue_channel_action.triggered.connect(self.show_channels)

        # Negative image connection
        self.negative_action.triggered.connect(self.show_negative)

        # Image rotation connections
        self.rotate_angle_spinbox.valueChanged.connect(self.rotate_image)
        self.turl_left_5_btn.pressed.connect(self.increase_current_rotation_angle_by_5_left)
        self.turn_right_5_btn.pressed.connect(self.increase_current_rotation_angle_by_5_right)

        # Draw circle connection
        self.draw_circle_instr.pressed.connect(self.draw_circle)