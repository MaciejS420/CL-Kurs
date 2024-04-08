import math


class Calculator:

    def __init__(self):
        self.results = []

    def add(self, n1, n2):
        result = n1 + n2
        self.results.append(f"add {n1} to {n2} got {result}")
        return result

    def multiply(self, n1, n2):
        result = n1 * n2
        self.results.append(f"multiplied {n1} by {n2} got {result}")
        return result

    def print_operations(self):
        for operation in self.results:
            print(operation)


# a = Calculator()
# b = Calculator()
# wynik = a.add(2,4)
# wynik = a.add(2,5)
# wynik = a.add(2,6)
# wynik = a.add(2,7)
# a.print_operations()
# print("_______________________")
# b.print_operations()

class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f"informacja o kształcie {self.x} {self.y}")

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"


# a = Shape(0,0,'blue')
# b = Shape(2,2,'red')
#
# print(a.distance(b))
# print(b.distance(a))


class BankAccount:

    def __init__(self, number):
        self.cash = 0
        self.number = number

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if amount > 0:
            if amount > self.cash:
                amount = self.cash
            self.cash -= amount
            return amount

    def print_info(self):
        print(self.number, self.cash)


# account = BankAccount(100)
# account.print_info()
# account.deposit_cash(100)
# account.print_info()
# account.deposit_cash(100)
# account.print_info()
# account.deposit_cash(-100)
# account.print_info()
# x = account.withdraw_cash(1)
# print(x)
# account.print_info()
# x = account.withdraw_cash(400)
# print(x)
# account.print_info()

class Employee:

    def __init__(self, id, imie, nazwisko):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self._salary = None

    def set_salary(self, salary):
        if type(salary) in (int, float) and salary > 0:
            self._salary = salary


class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f"informacja o kształcie {self.x} {self.y}")

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    # def __str__(self):
    #     return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"

class Circle(Shape):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self.r = r