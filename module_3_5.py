def get_multiplied_digits(number): # функция с параметром number
    str_number = str(number) # число в строку
    first = int(str_number[0]) # первый символ str_number в числовом представлении(int)

    if len(str_number) > 1: # Если длина str_number больше 1
        # возвращает значение first * get_multiplied_digits(int(str_number[1:]))
        # рекурсивный вызов функции с числом без первой цифры
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first # длина str_number не больше 1 возврат значения "first"

# Например:
result1 = get_multiplied_digits(2910109)
result2= get_multiplied_digits(91010)
print(result1)
print(result2)