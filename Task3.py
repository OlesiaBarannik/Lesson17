class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        if denominator == 0:
            raise ValueError("Denominator can't be zero!")

        self._denominator = denominator

    @staticmethod
    def LCM(num1: int, num2: int):
        if num1 > num2:
            greater = num1
        else:
            greater = num2

        while True:
            if (greater % num1 == 0) and (greater % num2 == 0):
                lcm = greater
                break
            greater += 1

        return lcm

    def __add__(self, other):
        lcm = self.LCM(self.denominator, other.denominator)
        num1 = self.numerator * (lcm // self.denominator)
        num2 = other.numerator * (lcm // other.denominator)
        numerator = num1 + num2

        return Fraction(numerator, lcm)

    def __sub__(self, other):
        lcm = LCM(self.denominator, other.denominator)
        num1 = self.numerator * (lcm // self.denominator)
        num2 = other.numerator * (lcm // other.denominator)
        numerator = num1 - num2

        return Fraction(numerator, lcm)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return Fraction(numerator, denominator)

    def __eq__(self, other):
        lcm = LCM(self.denominator, other.denominator)
        num1 = self.numerator * (lcm // self.denominator)
        num2 = other.numerator * (lcm // other.denominator)

        return num1 == num2

    def __lt__(self, other):
        lcm = LCM(self.denominator, other.denominator)
        num1 = self.numerator * (lcm // self.denominator)
        num2 = other.numerator * (lcm // other.denominator)

        return num1 < num2

    def __le__(self, other):
        lcm = LCM(self.denominator, other.denominator)
        num1 = self.numerator * (lcm // self.denominator)
        num2 = other.numerator * (lcm // other.denominator)

        return num1 <= num2

    def __float__(self):
        return self.numerator / self.denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


k = Fraction(1, 2)
print(float(Fraction(3, 4)))
print(float(Fraction(1, 2)) == float(Fraction(4, 8)))
print(k.__add__(0))
print(k.__add__(4))