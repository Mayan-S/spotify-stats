from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
from page7 import Ui_Form as Page7Form  

import PyQt5
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, False)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, False)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 960)
        Form.setFixedSize(Form.size())
        Form.setStyleSheet("background-image: url(:/backgrounds6/background_6.jpg);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 325, 440, 500))
        self.label.setStyleSheet("""
            color: black;
            font-weight: bold;
            font-size: 12pt;
            font-family: 'Arial';
        """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setAutoFillBackground(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Form = Form

        self.total_tracks = 0
        self.skipped_tracks = 0

        Form.mousePressEvent = self.mousePressEvent

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spotify Stats"))
        self.label.setText(_translate("Form", ""))

    def set_top_album(self, album_play_counts, total_tracks, skipped_tracks):
        self.total_tracks = total_tracks
        self.skipped_tracks = skipped_tracks

        if not album_play_counts:
            self.label.setText("No albums found.")
            return

        top_album = max(album_play_counts.items(), key=lambda x: x[1])
        album_name, play_count = top_album
        self.label.setText(f"{album_name}\n{play_count} plays")

    def mousePressEvent(self, event):
        self.show_page7()

    def show_page7(self):
        self.page7_window = QtWidgets.QWidget()
        self.page7_ui = Page7Form()
        self.page7_ui.setupUi(self.page7_window)

        self.page7_ui.set_completion_rate(self.total_tracks, self.skipped_tracks)

        self.Form.close()
        self.page7_window.show()
