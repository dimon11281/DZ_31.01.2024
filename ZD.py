"""Создать базовый класс Фигура с методом для подсчета
площади. Создать производные классы: прямоугольник,
круг, прямоугольный треугольник, трапеция со своими
методами для подсчета площади."""


from abc import ABC, abstractmethod
import math


def enter_fig(request):
    x = int(input(f"Введите {request} "))
    return x


class Figure:

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __int__(self):
        pass


class Rectangle(Figure):

    def __init__(self):
        self.width = enter_fig("ширину")
        self.height = enter_fig("высоту")

    def __int__(self, width, height):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник шириной - {self.width}, высотой - {self.height}, и площадью - {self.__int__(self.width, self.height)}"


class Cicle(Figure):

    def __init__(self):
        self.radius = enter_fig("радиус")

    def __int__(self, radius):
        return self.radius ** 2 * math.pi

    def __str__(self):
        return f"Круг имеет радиус - {self.radius} и площадь - {self.__int__(self.radius)}"


class Triangle(Figure):

    def __init__(self):
        self.katet1 = enter_fig("катет 1")
        self.katet2 = enter_fig("катет 2")

    def __int__(self, katet1, katet2):
        return self.katet1 * self.katet2 / 2

    def __str__(self):
        return f"Прямоугольный треугольник имеет катет - {self.katet1}, катет 2 - {self.katet2} и площадь - {self.__int__(self.katet1, self.katet2)}"


class Trapezoid(Figure):

    def __init__(self):
        self.footing1 = enter_fig("основание 1")
        self.footing2 = enter_fig("основание 2")
        self.height = enter_fig("высоту")

    def __int__(self, footing1, footing2, height):
        return (self.footing1 * self.footing2) / 2 * self.height

    def __str__(self):
        return f"Трапеция имеет основание 1 - {self.footing1}, основание 2 - {self.footing2}, высоту - {self.height} и площадь - {self.__int__(self.footing1, self.footing2, self.height)}"





# h1 = Rectangle()
# h2 = Rectangle()
# h3 = Rectangle()
# h1 = Cicle()
# h2 = Cicle()
# h3 = Cicle()
# h1 = Triangle()
# h2 = Triangle()
# h3 = Triangle()
h1 = Trapezoid()
h2 = Trapezoid()
h3 = Trapezoid()


print(h1)
print(h2)
print(h3)



"""Создайте базовый класс Shape для рисования плоских
фигур.
Определите методы:
■ Show() — вывод на экран информации о фигуре;
■ Save() — сохранение фигуры в файл;
■ Load() — считывание фигуры из файла.
Определите производные классы:
■ Square — квадрат, который характеризуется коорди-
натами левого верхнего угла и длиной стороны;
■ Rectangle — прямоугольник с заданными координа-
тами верхнего левого угла и размерами;
■ Circle — окружность с заданными координатами цен-
тра и радиусом;
■ Ellipse — эллипс с заданными координатами верхнего
угла описанного вокруг него прямоугольника со сто-
ронами, параллельными осям координат, и размерами
этого прямоугольника.
Создайте список фигур, сохраните фигуры в файл,
загрузите в другой список и отобразите информацию о
каждой из фигур."""