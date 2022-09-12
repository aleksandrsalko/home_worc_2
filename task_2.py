# Напишите программу, которая принимает на вход число N и выдает набор произведений 
# (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print('Должно быть целое число!')
    return number


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = InputNumbers("Введите число N: ")

list = []
for e in range(1, num + 1):
    list.append(factorial(e))

print(f"Произведения чисел от 1 до {num}:  {list}")    