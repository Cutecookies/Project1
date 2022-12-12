import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup, QPushButton, QGroupBox, QWidget
from random import randint, shuffle
from PyQt5.QtWidgets import QApplication


class Program(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() буду выносить всю настройку интерфейса,
        # чтобы не перегрузить инициализатор
        self.initui()

    def initui(self):
        # создание окна
        self.setGeometry(300, 100, 738, 600)
        self.setWindowTitle("Лото")

        self.h = 0  # переменная, помогающая опредилить концовку
        self.stat = 0  # переменная, необходимая для выведения статистики
        self.wins = self.loses = 0  # прибавление побед и проигрышей

        self.a = 1  # сменять билет, при нажатии на self.btn2
        self.numbers = [str(i) for i in range(1, 91)]
        shuffle(self.numbers)  # список цифр
        self.k1 = self.k2 = 0  # количество нажатых кнопок

        self.btn0 = QPushButton(self)  # создаю кнопку смены билета
        self.btn0.setText("Статистика")
        self.btn0.move(600, 340)
        self.btn0.resize(120, 51)
        self.btn0.clicked.connect(self.show_stat)

        self.btn1 = QPushButton(self)  # создаю кнопку начала игры
        self.btn1.setText("Начать игру")
        self.btn1.move(600, 400)
        self.btn1.resize(120, 51)
        self.btn1.clicked.connect(self.start)

        self.btn2 = QPushButton(self)  # создаю кнопку смены билета
        self.btn2.setText("Сменить билет")
        self.first_num = True
        self.btn2.move(600, 460)
        self.btn2.resize(120, 51)
        self.btn2.clicked.connect(self.group)

        self.label = QtWidgets.QLabel(self)
        self.label.move(580, 20)
        self.label.resize(121, 41)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.label_2 = QtWidgets.QLabel(self)  # создаю виджет, который будет
        self.label_2.move(590, 90)  # показывать текущее число
        self.label_2.resize(111, 111)
        font = QtGui.QFont()
        font.setPointSize(75)
        self.label_2.setFont(font)
        self.label_2.setText("")

        self.label_3 = QtWidgets.QLabel(self)  # создаю виджет, который будет
        self.label_3.move(550, 250)  # показывать результат игры
        self.label_3.resize(151, 41)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setText("")

        self.groupBox = QGroupBox("Билет соперника", self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.move(20, 10)
        self.groupBox.resize(481, 241)

        self.groupBox_2 = QGroupBox("Ваш билет", self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.move(20, 290)
        self.groupBox_2.resize(481, 241)

        self.group1 = QButtonGroup()
        self.group2 = QButtonGroup()
        self.n1 = []  # список кнопок 1 группы
        self.n2 = []  # список кнопок 2 группы

        f = 20
        for _ in range(5):  # создание кнопок 1 билета
            s = 20
            for _ in range(3):
                self.btn = QPushButton(self.groupBox)
                self.btn.move(f, s)
                self.btn.resize(75, 61)
                a = str(randint(1, 90))
                while a in self.n1:
                    a = str(randint(1, 90))
                self.n1.append(a)
                font = QtGui.QFont()
                font.setPointSize(10)  # создаю размер шрифта и цвет кнопки
                self.btn.setStyleSheet('QPushButton {background: #98FB98}')
                self.btn.setFont(font)
                self.btn.setText(a)
                self.group1.addButton(self.btn)
                s += 70
            f += 90

        f = 20
        for _ in range(5):  # создание кнопок 2 билета
            s = 20
            for _ in range(3):
                self.btn = QPushButton(self.groupBox_2)
                self.btn.move(f, s)
                self.btn.resize(75, 61)
                a = str(randint(1, 90))
                while a in self.n2:
                    a = str(randint(1, 90))
                self.n2.append(a)
                font = QtGui.QFont()
                font.setPointSize(10)  # создаю размер шрифта и цвет кнопки
                self.btn.setStyleSheet('QPushButton {background: #FFC0CB}')
                self.btn.setFont(font)
                self.btn.setText(a)
                self.btn.clicked.connect(self.check)
                self.group2.addButton(self.btn)
                s += 70
            f += 90

    def check(self):  # проверка: правильная ли кнопка нажата?
        num = self.btn.sender()
        if num.text() == self.label_2.text():
            self.k2 += 1
            num.setStyleSheet('QPushButton {background: #C71585;'
                              'color: white}')
            num.setEnabled(False)
        if self.k2 == 15:  # Победил игрок
            self.end_2(2)


    def start(self):  # начало игры: смена названия кнопок
        self.label.setText("Текущее число:")
        self.btn1.setText('Завершить игру')
        if self.first_num:
            self.btn2.setText('Первое число')
            self.first_num = False
        self.a = 0  # не сменять билет, при нажатии на self.btn2
        self.btn2.clicked.connect(self.game)
        self.btn1.clicked.connect(self.end)

    def end_2(self, num):  # концовка, если есть победитель
        for button in self.group1.buttons():
            button.setStyleSheet('QPushButton {background: #696969; '
                                 'color: white}')
            button.setEnabled(False)
        for button in self.group2.buttons():
            button.setStyleSheet('QPushButton {background: #696969; '
                                 'color: white}')
            button.setEnabled(False)
        self.btn2.setEnabled(False)

        self.h = 3  # закрытие игры при нажатии на self.btn1

        if num == 1:
            self.label_3.setText('Победил соперник')
            self.wins = 0
            self.loses = 1
        elif num == 2:
            self.label_3.setText('Вы победили')
            self.wins = 1
            self.loses = 0

    def game(self):
        self.btn2.setText('Следующее число')
        if len(self.numbers) > 3:  # проверка количества чисел
            n = self.numbers[0]
            self.numbers.remove(n)
            self.label_2.setText(n)

            lose_chance = [i for i in range(50)]  # шанс проиграть
            shuffle(lose_chance)
            random_num = lose_chance[0]

            if n in self.n1:  # игра за соперника
                if random_num != 1:
                    self.k1 += 1
                    for i in self.group1.buttons():
                        if i.text() == n:
                            i.setEnabled(False)
                            i.setStyleSheet(
                                'QPushButton {background: #006400; '
                                'color: white}')

            if self.k1 == 15:  # Победил соперник
                self.end_2(1)

        else:
            self.n1 = self.numbers[0]  # три оставшихся числа
            self.n2 = self.numbers[1]
            self.n3 = self.numbers[2]
            self.h = 1  # концовка, когда не осталось чисел
            self.end()

    def end(self):
        for button in self.group1.buttons():
            button.setStyleSheet('QPushButton {background: #696969; '
                                 'color: white}')
            button.setEnabled(False)
        for button in self.group2.buttons():
            button.setStyleSheet('QPushButton {background: #696969; '
                                 'color: white}')
            button.setEnabled(False)
        self.label.setText('')
        self.btn2.setEnabled(False)

        if self.h == 0:  # концовка после нажатия кнопки "Завершить игру"
            self.label_3.setText('Никто не победил.')
            self.label_2.setText('')
            self.h = 3  # закрытие игры при нажатии на self.btn1

        elif self.h == 1:  # концовка, когда не осталось чисел
            self.label.setText('Оставшиеся числа:')
            font = QtGui.QFont()
            font.setPointSize(10)
            self.label.setFont(font)
            self.label_3.setText('Никто не победил.')
            font = QtGui.QFont()
            font.setPointSize(18)
            self.label_2.setFont(font)
            self.label_2.setText(f'{self.n1}, {self.n2}, {self.n3}')
            self.h = 3  # закрытие игры при нажатии на self.btn1

        elif self.h == 3:  # закрытие игры
            self.close()

    def group(self):  # смена билета
        if self.a == 1:
            n2 = []
            for i in self.group2.buttons():
                a = str(randint(1, 90))
                while a in n2:
                    a = str(randint(1, 90))
                n2.append(a)
                i.setText(a)

    def show_stat(self):
        f = open("statistics.txt")  # чтение статистики
        data = [i for i in f.read().split()]
        f.close()
        wins = str(int(data[0]) + self.wins)  # добавление побед
        loses = str(int(data[1]) + self.loses)  # добавление проигрышей

        a = wins + ' ' + loses  # запись новой статистики
        f = open("statistics.txt", 'w')
        f.write(a)
        f.close()

        if self.stat == 0:  # вывод статистики
            self.save_num = self.label_2.text()  # сохранение текстов кнопок
            self.save_text = self.label.text()
            self.text3 = self.label_3.text()
            self.label_3.setText('')  # удаление текстов кнопок
            self.label.setText('')
            self.label_2.setText('')
            phrase = 'Победы: ' + wins + '\n' + 'Проигрыши: ' + loses
            self.label_3.setText(phrase)
            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            self.stat = 1

        elif self.stat == 1:  # скрытие статистики
            self.label.setText(self.save_text)  # возвращение текстов кнопок
            self.label_2.setText(self.save_num)
            self.label_3.setText(self.text3)
            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            self.stat = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
