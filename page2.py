from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
from page3 import Ui_Form as Page3Form

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 960)
        Form.setFixedSize(Form.size())
        Form.setStyleSheet("background-image: url(:/backgrounds2/background_2.jpg);")

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

        self.total_tracks = 0
        self.track_play_counts = {}
        self.artist_play_counts = {}
        self.album_play_counts = {}
        self.skipped_tracks = 0

        Form.mousePressEvent = self.mousePressEvent

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spotify Stats"))
        self.label.setText(_translate("Form", ""))

    def set_listening_time(self, minutes, total_tracks, track_play_counts, artist_play_counts, album_play_counts, skipped_tracks):
        self.label.setText(f"{minutes:,} minutes")
        self.total_tracks = total_tracks
        self.track_play_counts = track_play_counts
        self.artist_play_counts = artist_play_counts
        self.album_play_counts = album_play_counts
        self.skipped_tracks = skipped_tracks

    def mousePressEvent(self, event):
        self.show_page3()

    def show_page3(self):
        self.page3_window = QtWidgets.QWidget()
        self.page3_ui = Page3Form()
        self.page3_ui.setupUi(self.page3_window)

        self.page3_ui.set_total_tracks(
            self.total_tracks,
            self.track_play_counts,
            self.artist_play_counts,
            self.album_play_counts,
            self.skipped_tracks
        )

        self.Form.close()
        self.page3_window.show()
