def my_func(arg1, arg2, arg3):
    try:
        arg1 = float(input('Введите первое число: '))
        arg2 = float(input('Введите второе число: '))
        arg3 = float(input('Введите третье число: '))
        if arg1 >= arg3 and arg2 >= arg3:
            return round(arg1 + arg2, 2)
        elif arg1 > arg2 and arg1 < arg3:
            return round(arg1 + arg3, 2)
        else:
            return round(arg2 + arg3, 2)
    except ValueError:
        return 'Введено не число'
    except TypeError:
        return 'Введено не число'
print(my_func(1, 2, 3))