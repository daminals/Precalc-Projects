# OOP.py
# Daniel Kogan 6/24/2020
# Exploring method overloading through complex numbers

def main():
    class Complex:
        def __init__(self, real, imaginary):
            self.real = real
            self.imaginary = imaginary

        def __add__(self, other):
            return self.real + other.real, self.imaginary + other.imaginary

        def __sub__(self, other):
            return self.real - other.real, self.imaginary - other.imaginary

    ob1 = Complex(1, 5)
    ob2 = Complex(4, -3)

    print(ob1 + ob2)


if __name__ == '__main__':
    main()
