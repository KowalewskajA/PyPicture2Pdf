import random
import sys
import os

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QFileDialog)
from __feature__ import snake_case, true_property
from PIL import Image


class PyP2P(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.select_button = QPushButton("Select picture to convert to pdf")
        self.text = QLabel("Selected files:")
        self.file_label = QLabel("")
        self.convert_button = QPushButton("Convert file(s) to pdf")

        self.dialog = QFileDialog()
        self.dialog.file_mode = QFileDialog.ExistingFiles

        self.file_names = ""

        self.layout = QVBoxLayout(self)
        self.layout.add_widget(self.select_button)
        self.layout.add_widget(self.text)
        self.layout.add_widget(self.file_label)
        self.layout.add_widget(self.convert_button)


        # Connecting the signal
        self.select_button.clicked.connect(self.select_pictures)
        self.convert_button.clicked.connect(self.convert_pictures)

    @Slot()
    def select_pictures(self):
        if self.dialog.exec():
            #print(dir(self.dialog))
            self.file_names = self.dialog.selected_files()
            #print(self.fileNames)
            tmp = ""
            for name in self.file_names:
                tmp = tmp + name + "\n"
            self.file_label.text = tmp
    @Slot()
    def convert_pictures(self):

        for name in self.file_names:
            image = Image.open(name)
            pdf = image.convert('RGB')
            pdf.save(os.path.splitext(name)[0] + '.pdf')
        self.file_label.text = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = PyP2P()
    widget.show()

    sys.exit(app.exec())
