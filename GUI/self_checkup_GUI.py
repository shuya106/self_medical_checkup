import sys
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLCDNumber, QSlider, QVBoxLayout, QLineEdit, QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QInputDialog, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from keras.models import load_model
from Functions import process_img
import cv2
import numpy as np
from tiny_yolo import YOLO
from PIL import Image


class ExampleWidget():

    def __init__(self):
        super().__init__()
        self.resultR = {"sex": 0, "age":0, "kowabari":0, "img":0}
        self.modelR = load_model("Predict_model.h5")

        self.resultS = {"pain": 0, "ryuki":0, "ray":0, "img":0}
        self.yolo = YOLO()

        self.w = QWidget()
        self.w.title = "お悩みは？"

        self.buttonR = QPushButton("関節リウマチ", self.w)
        self.buttonR.move(20,70)
        self.buttonR.clicked.connect(self.R)

        self.buttonS = QPushButton("皮膚ガン", self.w)
        self.buttonS.move(20,150)
        self.buttonS.clicked.connect(self.S)


        self.w.resize(200,200)
        self.w.show()
    def R(self):
        self.R = QWidget()
        self.R.resize(300,300)
        self.R.title="関節リウマチ"

        self.R.button1 = QPushButton("判定", self.R)
        self.R.button1.move(200,200)
        self.R.button1.clicked.connect(self.judgeR)
        self.R.button2 = QPushButton("スキャン", self.R)
        self.R.button2.move(200, 150)
        self.R.button2.clicked.connect(self.scanR)
        self.R.ch1 = QCheckBox("女性ですか", self.R)
        self.R.ch1.move(30,40)
        self.R.ch1.stateChanged.connect(self.ch_sexR)
        self.R.ch2 = QCheckBox("40才以上ですか", self.R)
        self.R.ch2.move(30,80)
        self.R.ch2.stateChanged.connect(self.ch_ageR)
        self.R.ch3 = QCheckBox("朝30分以上手がこわばりますか", self.R)
        self.R.ch3.move(30,120)
        self.R.ch3.stateChanged.connect(self.ch_kowabariR)
        self.R.leR = QLineEdit(self.R)
        self.R.leR.move(150, 250)

        self.R.show()

    def scanR(self):

        self.imgR = process_img(["./res.png"])
        self.predR = self.modelR.predict(self.imgR)
        self.predR = np.argmax(self.predR)
        if self.predR == 1:
            self.predR = 0
        else:
            self.predR = 1
        self.resultR["img"] = self.predR

    def ch_sexR(self, state):
        if state == Qt.Checked:
            self.resultR["sex"] = 1
        else:
            self.resultR["sex"] = 0
    def ch_ageR(self, state):
        if state == Qt.Checked:
            self.resultR["age"] = 1
        else:
            self.resultR["age"] = 0
    def ch_kowabariR(self, state):
        if state == Qt.Checked:
            self.resultR["kowabari"] = 1
        else:
            self.resultR["kowabari"] = 0
    def judgeR(self):
        self.resR = sum(list(self.resultR.values()))
        if self.resR < 3:
            self.resR = 0
        else:
            self.resR = 1
        self.ansR = ["正常です", "病院へ行きましょう"]
        self.ansR = self.ansR[self.resR]

        self.R.leR.setText(str(self.ansR))

    def S(self):
        self.S = QWidget()
        self.S.resize(300,300)
        self.S.title="皮膚ガン"

        self.S.button1 = QPushButton("判定", self.S)
        self.S.button1.move(200,200)
        self.S.button1.clicked.connect(self.judgeS)
        self.S.button2 = QPushButton("スキャン", self.S)
        self.S.button2.move(200, 150)
        self.S.button2.clicked.connect(self.scanS)
        self.S.ch1 = QCheckBox("痛みはありますか", self.S)
        self.S.ch1.move(30,40)
        self.S.ch1.stateChanged.connect(self.ch_painS)
        self.S.ch2 = QCheckBox("患部は隆起していますか", self.S)
        self.S.ch2.move(30,80)
        self.S.ch2.stateChanged.connect(self.ch_ryukiS)
        self.S.ch3 = QCheckBox("普段から紫外線を多く浴びますか", self.S)
        self.S.ch3.move(30,120)
        self.S.ch3.stateChanged.connect(self.ch_rayS)
        self.S.leS = QLineEdit(self.S)
        self.S.leS.move(150, 250)

        self.S.show()

    def scanS(self):

        self.imgS = Image.open("2.jpg")
        self.predS = self.yolo.detect_image(self.imgS)

        if self.predS == 0:
            self.predS = 0
        else:
            self.predS = 1
        self.resultS["img"] = self.predS

    def judgeS(self):
        self.resS = sum(list(self.resultS.values()))
        if self.resS < 3:
            self.resS = 0
        else:
            self.resS = 1
        self.ansS = ["正常です", "病院へ行きましょう"]
        self.ansS = self.ansS[self.resS]

        self.S.leS.setText(str(self.ansS))
    def ch_painS(self, state):
        if state == Qt.Checked:
            self.resultS["pain"] = 1
        else:
            self.resultS["pain"] = 0
    def ch_ryukiS(self, state):
        if state == Qt.Checked:
            self.resultS["ryuki"] = 1
        else:
            self.resultS["ryuki"] = 0
    def ch_rayS(self, state):
        if state == Qt.Checked:
            self.resultS["ray"] = 1
        else:
            self.resultS["ray"] = 0







if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = ExampleWidget()
    sys.exit(app.exec_())
