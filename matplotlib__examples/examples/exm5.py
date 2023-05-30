__author__ = "ipetrash"


# По умолчанию создается окно, у которого ширина и высота различны, из-за чего "пирог"
# получается не круглый, а овальный. Для того, чтобы "пирог" стал круглый, окно нужно
# создать самостоятельно с помощью функции figure(), которая принимает параметр figsize,
# определяющий размер окна в дюймах (разрешение также можно указывать в параметрах, но
# на данный момент обойдемся без этого). Также с помощью функции axes() создадим оси,
# занимающее все окно.


import pylab

if __name__ == "__main__":
    # Данные для построения графика
    data = [20.0, 10.0, 5.0, 1.0, 0.5]

    # Создать новое окно (фигуру) с одинаковыми размерами сторон (6 x 6 дюйма)
    pylab.figure(figsize=(6, 6))

    # Установим размеры осей по горизонтали и вертикали тоже одинаковыми
    pylab.axes([0.0, 0.0, 1.0, 1.0])

    # И снова нарисуем график
    pylab.pie(data)

    pylab.show()
