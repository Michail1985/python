n = int(input('Введите число от 1 до 9: '))
temp = str(n)
temp1 = temp + temp
temp2 = temp1 + temp
n = n + int(temp1) + int(temp2)
print('Результат равен: ', n)
