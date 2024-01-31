"""Задание 1
Создайте класс Device, который содержит информацию об устройстве.
Спомощью механизма наследования, реализуйте класс
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы."""

class Device:

    def __init__(self, voltage=220, power=2, color="white"):
        self.__voltage = voltage
        self.__power = power
        self.__color = color

    def set_voltage(self, voltage):
        self.__voltage = voltage

    def get_voltage(self):
        return self.__voltage

    def set_power(self, power):
        self.__power = power

    def get_power(self):
        return self.__power

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class CoffeeMachine(Device):

    def __init__(self, voltage=110, power=7, color="grey", coffee_per_hour: int=20):
        super().__init__(voltage, power, color)
        self.__coffee_per_hour = coffee_per_hour

    def set_coffee_per_hou(self, coffee_per_hour):
        self.__coffee_per_hou = coffee_per_hour

    def get_coffee_per_hou(self):
        return self.__coffee_per_hour

    def __str__(self):
        return f"Данная кофемашина питается от {self.get_voltage()}, мощность - {self.get_power()}, цвет - {self.get_color()}, производительностью - {self.__coffee_per_hour}"


class Blender(Device):

    def __init__(self, voltage=220, power=6, color="зеленый", rpm: int=3000):
        super().__init__(voltage, power, color)
        self.__rpm = rpm

    def set_rpm(self, rpm):
        self.__rpm = rpm

    def get_rpm(self):
        return self.__rpm

    def __str__(self):
        return f"Данный блендер питается от {self.get_voltage()}, мощность - {self.get_power()}, цвет - {self.get_color()}, оборотов - {self.__rpm}"


class MeatGrinder(Device):

    def __init__(self, voltage=220, power=6, color="малиновый", processing_meat: int=5):
        super().__init__(voltage, power, color)
        self.__processing_meat = processing_meat

    def set_color(self, processing_meat):
        self.__processing_meat = processing_meat

    def get_processing_meat(self):
        return self.__processing_meat

    def __str__(self):
        return f"Данная мясорубка питается от {self.get_voltage()}, мощность - {self.get_power()}, цвет - {self.get_color()}, производит - {self.__processing_meat} кг. фарша в час."


# print(MeatGrinder(color="голубой"))


"""Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
поле для хранения копеек (центы, евроценты, копейки
и т.д.).
Реализовать методы для вывода суммы на экран, задания значений для частей."""

class Money:

    def __init__(self, rubles, kopeek):
        self.__rubles = rubles
        self.__kopeek = kopeek

    def set_rubles(self, rubles):
        self.__rubles = rubles

    def get_rubles(self):
        return self.__rubles

    def set_kopeek(self, kopeek):
        self.__kopeek = kopeek

    def get_kopeek(self):
        return self.__kopeek

    def add_deneg(self, other):
        new_rubles = self.get_rubles() + other.get_rubles()
        new_kopeek = self.get_kopeek() + other.get_kopeek()
        if new_kopeek >= 100:
            new_kopeek -= 100
            new_rubles += 1
        return Money(new_rubles, new_kopeek)

    def __str__(self):
        return f"Денег на счете - {self.get_rubles()},{self.get_kopeek()} "

m1 = Money(22, 18)
m3 = Money(33, 20)

print(m1.add_deneg(m3))









