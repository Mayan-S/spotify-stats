from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
from page6 import Ui_Form as Page6Form  

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 960)
        Form.setFixedSize(Form.size())
        Form.setStyleSheet("background-image: url(:/backgrounds5/background_5.jpg);")

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

    def set_top_artists(self, artist_play_counts, album_play_counts, total_tracks, skipped_tracks):
        self.artist_play_counts = artist_play_counts
        self.album_play_counts = album_play_counts
        self.total_tracks = total_tracks
        self.skipped_tracks = skipped_tracks

        sorted_artists = sorted(artist_play_counts.items(), key=lambda x: x[1], reverse=True)
        top_5 = sorted_artists[:5]

        if not top_5:
            self.label.setText("No artists found.")
            return

        text = ""
        for i, (artist, count) in enumerate(top_5, 1):
            text += f"{i}. {artist} - {count} plays\n\n"

        self.label.setText(text)

    def mousePressEvent(self, event):
        self.show_page6()

    def show_page6(self):
        self.page6_window = QtWidgets.QWidget()
        self.page6_ui = Page6Form()
        self.page6_ui.setupUi(self.page6_window)

        self.page6_ui.set_top_album(
            self.album_play_counts,
            self.total_tracks,
            self.skipped_tracks
        )

        self.Form.close()
        self.page6_window.show()
