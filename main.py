import sys
from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QtWidgets.QLabel()
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)

        self.close_button = QtWidgets.QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.addTab(QtWidgets.QWidget(), "Text")

        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        tab2_layout = QtWidgets.QVBoxLayout()
        tab2_layout.addWidget(self.video_widget)
        tab2_layout.addWidget(QtWidgets.QPushButton("Play", clicked=self.play_video))
        tab2_layout.addWidget(QtWidgets.QPushButton("Stop", clicked=self.stop_video))
        tab2 = QtWidgets.QWidget()
        tab2.setLayout(tab2_layout)
        self.tabs.addTab(tab2, "Videva")

        self.tabs.addTab(QtWidgets.QWidget(), "Audio")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QtCore.QTime.currentTime().toString('hh:mm:ss')
        self.time_label.setText(current_time)

    def play_video(self):
        video_url = "Path\to\cat.mp4"
        self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_url)))
        self.media_player.play()

    def stop_video(self):
        self.media_player.stop()

    def close(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Jetbrains mono", 10, QtGui.QFont.Bold))
    window = MyWindow()
    window.setWindowTitle("GoidaTube")
    window.resize(1280, 720)
    window.show()
    sys.exit(app.exec_())
