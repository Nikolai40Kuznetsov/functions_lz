def convert_temperature(a):
    return float(a) * 9 / 5 + 32
user_input = input("Введите температуру в градусах по Цельсию ")
print(f"Это {convert_temperature(user_input)} градусов по Фаренгейту")