def my_sum():
    prov = False
    sum_res = 0
    while prov == False:
        numbers = input('Введите числа или нажмите Q для выхода: ').split()
        res = 0
        for ell in range(len(numbers)):
            if numbers[ell] == 'Q' or numbers[ell] == 'q':
                prov = True
                break
            else:
                res = res + int(numbers[ell])
        sum_res += res
        print('Результат суммы чисел: ', sum_res)

my_sum()