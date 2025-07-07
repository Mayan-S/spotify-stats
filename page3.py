from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
from page4 import Ui_Form as Page4Form

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
        Form.setStyleSheet("background-image: url(:/backgrounds3/background_3.jpg);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 330, 440, 100))
        self.label.setStyleSheet("""
            color: white;
            font: 75 14pt 'Arial';
        """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setAutoFillBackground(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Form = Form

        self.track_play_counts = {}
        self.artist_play_counts = {}
        self.album_play_counts = {}
        self.total_tracks = 0
        self.skipped_tracks = 0

        Form.mousePressEvent = self.mousePressEvent

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spotify Stats"))
        self.label.setText(_translate("Form", ""))

    def set_total_tracks(self, total_tracks, track_play_counts, artist_play_counts, album_play_counts, skipped_tracks):
        self.label.setText(f"{total_tracks:,} tracks played")
        self.total_tracks = total_tracks
        self.track_play_counts = track_play_counts
        self.artist_play_counts = artist_play_counts
        self.album_play_counts = album_play_counts
        self.skipped_tracks = skipped_tracks

    def mousePressEvent(self, event):
        self.show_page4()

    def show_page4(self):
        self.page4_window = QtWidgets.QWidget()
        self.page4_ui = Page4Form()
        self.page4_ui.setupUi(self.page4_window)

        self.page4_ui.set_top_tracks(
            self.track_play_counts,
            self.artist_play_counts,
            self.album_play_counts,
            self.total_tracks,
            self.skipped_tracks
        )

        self.Form.close()
        self.page4_window.show()
