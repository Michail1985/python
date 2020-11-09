summa = 0
try:
    prov = float(input('Введите первое число:'))
    summa = prov
    with open('file_name5.txt', 'w') as my_file:
        summa_count = (f'{prov}\x20')
        while my_file:
            try:
                prov = float(input('Введите следующее число:'))
                summa = summa + prov
                summa_count = summa_count + (f'{prov}\x20')
            except ValueError:
                break
        print('Сумма чисел равна:', summa)
        my_file.write(summa_count)
except ValueError:
    print('Файл не создан!', '\nСумма чисел равна:', summa)