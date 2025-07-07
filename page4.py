from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
from page5 import Ui_Form as Page5Form  

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
        Form.setStyleSheet("background-image: url(:/backgrounds4/background_4.jpg);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 200, 440, 800))
        self.label.setStyleSheet("""
            color: black;
            font-weight: bold;
            font-size: 12pt;
            font-family: 'Arial';
        """)
        self.label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setAutoFillBackground(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Form = Form

        self.artist_play_counts = {}
        self.album_play_counts = {}
        self.total_tracks = 0
        self.skipped_tracks = 0

        Form.mousePressEvent = self.mousePressEvent

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spotify Stats"))
        self.label.setText(_translate("Form", ""))

    def set_top_tracks(self, track_play_counts, artist_play_counts, album_play_counts, total_tracks, skipped_tracks):
        self.artist_play_counts = artist_play_counts
        self.album_play_counts = album_play_counts
        self.total_tracks = total_tracks
        self.skipped_tracks = skipped_tracks

        sorted_tracks = sorted(track_play_counts.items(), key=lambda x: x[1], reverse=True)
        top_5 = sorted_tracks[:5]

        if not top_5:
            self.label.setText("No tracks found.")
            return

        text = ""
        for i, (track, count) in enumerate(top_5, 1):
            text += f"{i}. {track} - {count} plays\n\n"

        self.label.setText(text)

    def mousePressEvent(self, event):
        self.show_page5()

    def show_page5(self):
        self.page5_window = QtWidgets.QWidget()
        self.page5_ui = Page5Form()
        self.page5_ui.setupUi(self.page5_window)

        self.page5_ui.set_top_artists(
            self.artist_play_counts,
            self.album_play_counts,
            self.total_tracks,
            self.skipped_tracks
        )

        self.Form.close()
        self.page5_window.show()
