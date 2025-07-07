from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

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
        Form.setStyleSheet("background-image: url(:/backgrounds7/background_7.jpg);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 230, 440, 500))
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

        Form.mousePressEvent = self.mousePressEvent

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spotify Stats"))
        self.label.setText(_translate("Form", ""))

    def set_completion_rate(self, total_tracks, skipped_tracks):
        if total_tracks == 0:
            self.label.setText("No tracks found.")
            return

        completed = total_tracks - skipped_tracks
        rate = (completed / total_tracks) * 100
        self.label.setText(f"There is a {rate:.2f}%\n chance that you\nwill listen to a\nsong entirely!")

    def mousePressEvent(self, event):
        QtWidgets.QMessageBox.information(
            None,
            "The End!",
            "This is the last page.\nThank you for using Spotify Stats!"
        )
        QtWidgets.QApplication.quit()
