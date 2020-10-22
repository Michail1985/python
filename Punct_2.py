i = int(input('Введите время в секундах: '))
minuta = i // 60
secunda = i % 60
chas = minuta // 60
minuta = minuta % 60
print('Время: ', chas, ": ", minuta, ': ', secunda)
