try:
    number = int(input("Введите целое положительное число - "))
    if  number >= 0:
        while number >= 0:
            print(number)
            number -= 1
    else:
        print("Вы ввели отрицательно число.")
except ValueError:
    print("Ошибка: введено число не соответствующее параметрам ввода!!!")
