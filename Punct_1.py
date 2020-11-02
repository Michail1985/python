def my_funct(chis_1, chis_2):
    try:
        chis_1 = float(input('Введите первое число: '))
        chis_2 = float(input('Введите первое число: '))
        answer = round(chis_1 / chis_2, 2)
    except ValueError:
        return 'Введено не число'
    except ZeroDivisionError:
        return 'Деление на ноль'
    return answer
print(my_funct(1, 2))