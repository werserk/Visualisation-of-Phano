import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        self.setupUi(self)
        self.btnAddCode.clicked.connect(self.addCode)
        self.btnAddLetter.clicked.connect(self.addLetter)

    def addCode(self):
        self.canvas.letters.append((self.editCode.text(), ' '))
        self.canvas.update()

    def addLetter(self):
        for i, (code, letter) in enumerate(self.canvas.letters):
            if code == self.editCode.text():
                self.canvas.letters[i] = (code, self.editLetter.text())
                break
        else:
            self.canvas.letters.append((self.editCode.text(), self.editLetter.text()))
        self.canvas.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
