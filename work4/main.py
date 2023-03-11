class BaseMachine:
    """базовый класс - Станок"""

    def __init__(self, a_val, b_val, c_val):
        # a - производительность изделий в час
        # b - стоимость станка
        # c - средняя цена детали
        self.a = a_val
        self.b = b_val
        self.c = c_val

    def __str__(self):
        string = "производительность изделий в час: " + \
                 str(self.a) + "\n" + \
                 "стоимость станка: " + \
                 str(self.b) + "\n" + \
                 "средняя цена детали: " + \
                 str(self.c) + "\n"
        return string

    def __add__(self, other):
        """суммируем только производительность изделий в час"""
        if isinstance(other, self.__class__):
            self.a += other.a
            return self.__class__(self.a + other.a,
                                  self.b,
                                  self.c)
        elif isinstance(other, (int, int, int)):
            return self.__class__(self.a + other,
                                  self.b,
                                  self.c)
        else:
            raise TypeError(
                f'Не могу добавить {self.__class__} к {type(other)}'
            )

    def __radd__(self, other):
        return self + other

    # кол-во деталей до окупаемости
    def get_details_num_for_payback(self):
        if self.c == 0:
            raise ValueError("ошибка - нулевая средняя цена")
        return self.b / self.c

    # время окупаемости станка
    def get_time_for_payback(self):
        return self.get_details_num_for_payback()*self.a

    @staticmethod
    def sum_machines_efficiency(*machines):
        """суммируем набор из станков"""
        # за базовый берем первый станок из списка
        # его параметры, которые не суммируются,
        # будут в новом экземпляре
        new_machine = BaseMachine(0, 0, 0)
        for machine in machines:
            new_machine = new_machine + machine
        return new_machine


class MillingMachine(BaseMachine):
    """фрезерный станок"""
    def __init__(self, a_val, b_val, c_val, d_val="unknown"):
        super().__init__(a_val, b_val, c_val)
        # d - наименование производителя
        self.d = d_val

    def __str__(self):
        return super().__str__() + \
            "наименование производителя: " + \
            str(self.d) + "\n"

    def __add__(self, other):
        """суммируем только производительность изделий в час"""
        if isinstance(other, self.__class__):
            return self.__class__(self.a + other.a,
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, (int, int, int)):
            return self.__class__(self.a + other,
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, tuple):
            a = other
            return self.__class__(self.a + a[0],
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, BaseMachine):
            return self.__class__(self.a + other.a,
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, CncMachine):
            return self.__class__(self.a + other.a,
                                  self.b,
                                  self.c,
                                  self.d)
        else:
            raise TypeError(
                f'Не могу добавить {self.__class__} к {type(other)}'
            )

    def __radd__(self, other):
        return self + other


class CncMachine(BaseMachine):
    """ЧПУ станок"""
    def __init__(self, a_val, b_val, c_val, d_val):
        super().__init__(a_val, b_val, c_val)
        # d - кол-во сменных инструментов
        self.d = d_val

    def __str__(self):
        return super().__str__() + \
            "кол-во сменных инструментов: " + \
            str(self.d) + "\n"

    def __add__(self, other):
        """суммируем только производительность изделий в час"""
        if isinstance(other, self.__class__):
            return self.__class__(self.a + other.a,
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, (int, int, int)):
            return self.__class__(self.a + other,
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, tuple):
            a = other
            return self.__class__(self.a + a[0],
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, BaseMachine):
            return self.__class__(self.a + other.a,
                                  self.b,
                                  self.c,
                                  self.d)
        elif isinstance(other, MillingMachine):
            return self.__class__(self.a + other.a,
                                  self.b,
                                  self.c,
                                  self.d)
        else:
            raise TypeError(
                f'Не могу добавить {self.__class__} к {type(other)}'
            )

    def __radd__(self, other):
        return self + other


print("-------------------------------------------")
print("Проверка работы с базовым классом")
print("-------------------------------------------")
m = BaseMachine(1, 100, 1)
num = m.get_details_num_for_payback()
num1 = m.get_time_for_payback()
print("m:")
print(m)
print(f"кол-во деталей до окупаемости :  {num} \n")
print(f"время до окупаемости :  {num1} \n")
print("-------------------------------------------")
m1 = BaseMachine(2, 200, 2)
m2 = m1 + m
print("m2:")
print(m2)
# m3 = 4
# m4 = m3 + m2
print("-------------------------------------------")
m5 = BaseMachine.sum_machines_efficiency(m, m1, m2, BaseMachine(1, 1, 1))
print("m5:")
print(m5)
print("-------------------------------------------")
print("работа с потомками")
print("-------------------------------------------")
print("сложение с кортежем \n")
m6 = MillingMachine(3, 600, 1, "BAUHAUS")
print("m6:")
print(m6)
print("m7:")
m7 = m6 + (2, 200, 2)
print(m7)
print("-------------------------------------------")
print("сложение с другим типом \n")
m8 = m6 + BaseMachine(2, 200, 2)
print("m8:")
print(m8)
print("-------------------------------------------")
m9 = CncMachine(3, 1000, 3, 10)
print("m9:")
print(m9)
m10 = m9 + BaseMachine(2, 200, 2) + MillingMachine(3, 600, 1, "BAUHAUS")
print("m10:")
print(m10)
m11 = BaseMachine.sum_machines_efficiency(
    CncMachine(3, 1000, 3, 10),
    BaseMachine(2, 200, 2),
    MillingMachine(3, 600, 1, "BAUHAUS")
    )
print("m11:")
print(m11)
