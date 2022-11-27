from UI2 import Ui_Form
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtCore import Qt
from playsound import playsound



class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_mp3('/Users/sidratmirzoev/PycharmProjects/PyGraph/do.mp3')
        self.load_mp4('/Users/sidratmirzoev/PycharmProjects/PyGraph/Do-2.mp3')
        self.load_mp5('/Users/sidratmirzoev/PycharmProjects/PyGraph/si.mp3')
        self.load_mp6('/Users/sidratmirzoev/PycharmProjects/PyGraph/re.mp3')
        self.load_mp7('/Users/sidratmirzoev/PycharmProjects/PyGraph/mi.mp3')
        self.load_mp8('/Users/sidratmirzoev/PycharmProjects/PyGraph/sol.mp3')
        self.load_mp9('/Users/sidratmirzoev/PycharmProjects/PyGraph/fa.mp3')
        self.load_mp10('/Users/sidratmirzoev/PycharmProjects/PyGraph/lja.mp3')
        self.load_mp11('/Users/sidratmirzoev/PycharmProjects/PyGraph/All.mp3')
        self.Do.clicked.connect(self.player.play)
        self.Do_2.clicked.connect(self.player1.play)
        self.Ci.clicked.connect(self.player2.play)
        self.Re.clicked.connect(self.player3.play)
        self.Mi.clicked.connect(self.player4.play)
        self.Fa.clicked.connect(self.player6.play)
        self.Sol.clicked.connect(self.player5.play)
        self.La.clicked.connect(self.player7.play)
        self.All.clicked.connect(self.player8.play)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/do.mp3')
        if event.key() == Qt.Key_R:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/re.mp3')
        if event.key() == Qt.Key_M:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/mi.mp3')
        if event.key() == Qt.Key_F:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/fa.mp3')
        if event.key() == Qt.Key_S:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/sol.mp3')
        if event.key() == Qt.Key_L:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/lja.mp3')
        if event.key() == Qt.Key_C:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/si.mp3')
        if event.key() == Qt.Key_2:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/Do-2.mp3')
        if event.key() == Qt.Key_Space:
            playsound('/Users/sidratmirzoev/PycharmProjects/PyGraph/All.mp3')



    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
    def load_mp4(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player1 = QtMultimedia.QMediaPlayer()
        self.player1.setMedia(content)
    def load_mp5(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player2 = QtMultimedia.QMediaPlayer()
        self.player2.setMedia(content)
    def load_mp6(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player3 = QtMultimedia.QMediaPlayer()
        self.player3.setMedia(content)
    def load_mp7(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player4 = QtMultimedia.QMediaPlayer()
        self.player4.setMedia(content)
    def load_mp8(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player5 = QtMultimedia.QMediaPlayer()
        self.player5.setMedia(content)
    def load_mp9(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player6 = QtMultimedia.QMediaPlayer()
        self.player6.setMedia(content)
    def load_mp10(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player7 = QtMultimedia.QMediaPlayer()
        self.player7.setMedia(content)
    def load_mp11(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player8 = QtMultimedia.QMediaPlayer()
        self.player8.setMedia(content)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())