a = int(input('Ввести киллометры для первогодня: '))
b = int(input('Ввести желаемый результат: '))
denn = 0
while True:
    denn += 1
    denn_str = str(denn) + '-й день'
    print(denn_str, ': ', a)
    if a <= b:
        a = round(a * 1.1, 2)
    else:
        print('Ответ: на ', denn_str, ' спортсмен достигнет результата — не менее ', b, ' км.')
        break
