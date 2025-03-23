try:
    number = int(input("Введите целое положительное число - "))

    while number >= 0:
        print(number)
        number -= 1
    else:
        print("Введенно не целое положительное число. ")
except ValueError:
    print("Ошибка: введено число не соответствующее параметрам ввода!!!")
