from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import json
from collections import defaultdict
import resources_rc
from page2 import Ui_Form as Page2Form

import PyQt5
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, False)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, False)
    
class Ui_MainForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 960)
        Form.setFixedSize(Form.size())
        Form.setStyleSheet("background-image: url(:/backgrounds/main_menu_background.jpg);")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(135, 780, 270, 100))
        self.pushButton.setStyleSheet(
            "background-image: url(:/backgrounds/white_background.jpg);\n"
            "font: 75 15pt \"8514oem\";"
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("UPLOAD JSON FILES")
        self.pushButton.clicked.connect(self.upload_json_files)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Form = Form 

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spotify Stats"))

    def upload_json_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            None,
            "Select JSON Files",
            "",
            "JSON Files (*.json);;All Files (*)"
        )

        if not files:
            return

        total_ms = 0
        total_tracks = 0
        skipped_tracks = 0
        track_play_counts = defaultdict(int)
        artist_play_counts = defaultdict(int)
        album_play_counts = defaultdict(int)

        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                except Exception as e:
                    QMessageBox.critical(None, "Encoding Error", f"Failed to decode {file_path}:\n{str(e)}")
                    continue
            except Exception as e:
                QMessageBox.critical(None, "File Error", f"Failed to open {file_path}:\n{str(e)}")
                continue

            for entry in data:
                if isinstance(entry, dict):
                    if 'ms_played' in entry:
                        total_ms += entry['ms_played']

                    track_name = entry.get('master_metadata_track_name')
                    artist_name = entry.get('master_metadata_album_artist_name')
                    album_name = entry.get('master_metadata_album_album_name')

                    if track_name:
                        total_tracks += 1
                        track_play_counts[track_name] += 1

                    if artist_name:
                        artist_play_counts[artist_name] += 1

                    if album_name:
                        album_play_counts[album_name] += 1

                    if entry.get("skipped") is True:
                        skipped_tracks += 1

        total_minutes = round(total_ms / 60000)

        self.show_page2(
            total_minutes,
            total_tracks,
            track_play_counts,
            artist_play_counts,
            album_play_counts,
            skipped_tracks
        )

    def show_page2(self, total_minutes, total_tracks, track_play_counts, artist_play_counts, album_play_counts, skipped_tracks):
        self.page2_window = QtWidgets.QWidget()
        self.page2_ui = Page2Form()
        self.page2_ui.setupUi(self.page2_window)

        self.page2_ui.set_listening_time(
            total_minutes,
            total_tracks,
            track_play_counts,
            artist_play_counts,
            album_play_counts,
            skipped_tracks
        )

        self.Form.close()
        self.page2_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
