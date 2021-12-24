from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush


class Canvas(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Canvas, self).__init__(*args, **kwargs)
        self.text = 'корень'
        self.letters = [('01', 'A'), ('1', 'B')]
        self.font = QFont('Helvetica [Cronyx]')
        # self.font.setPointSize(18)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        root_text = QtGui.QFontMetricsF(self.font).boundingRect(self.text)
        center_x = self.width() // 2 - root_text.width() // 2
        center_y = max(self.height() // 10 - root_text.height(), root_text.height())
        qp.drawText(center_x - root_text.width() // 2, center_y, self.text)

        y_step = len(max(self.letters, key=lambda x: len(x[0]))[0]) + 1
        self.letters = sorted(self.letters, )
        for i, (code, letter) in enumerate(self.letters):
            text = QtGui.QFontMetricsF(self.font).boundingRect(letter)
            _code = ''
            x1 = center_x
            y1 = center_y
            while len(_code) < len(code):
                _code += code[len(_code)]
                step = len(_code) + 1
                y = y1 + self.height() // y_step
                x = x1
                if int(_code[-1]) == 1:
                    x += self.width() // (2 ** step)
                else:
                    x -= self.width() // (2 ** step)
                x -= text.width() // 2
                x = max(x, text.width())
                x0 = x1
                y0 = y1
                x1 = x + text.width() // 2
                y1 = y
                qp.drawLine(x0, y0, x1, y1)
                qp.drawText((x0 + x1) // 2, (y0 + y1) // 2, _code[-1])
                qp.setBrush(QBrush(QColor(0, 0, 0)))
                qp.drawEllipse(x1 - 2, y1 - 2, 4, 4)
            qp.drawText(x, y, letter)
