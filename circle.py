from math import pi
def area(a):
    return pi * int(a) * int(a)
def circumference(a):
    return int(a) * pi * 2
user_input = input("Введите радиус круга ")
print(f"Длина окружности: {circumference(user_input)} единиц")
print(f"Площадь круга: {area(user_input)} квадратных единиц")