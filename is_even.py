def is_even(a):
    if a % 2 == 0:
        return("Число является чётным")
    else:
        return("Число является нечётным")
user_input = int(input("Введите число "))
print(is_even(user_input))
