import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime
from GATS import gats_time


class GATSGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Global Adaptive Time System')

        vbox = QVBoxLayout()

        self.gats_label = QLabel()
        vbox.addWidget(self.gats_label)

        self.setLayout(vbox)

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        self.update_time()

    def update_time(self):
        local_time = gats_time()
        time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
        self.gats_label.setText(f'GATS Time: {time_str}')


def main():
    app = QApplication(sys.argv)
    ex = GATSGUI()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
