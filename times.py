def convert_time(a, b, c):
    return int(a) * 3600 + int(b) * 60 + int(c)
user_input = input("Введите время ")
hours, minutes, seconds = user_input.split("-")
print(f"Это {convert_time(hours, minutes, seconds)} cекунд")
