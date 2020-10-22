viruchka = int(input('Введите значение выручки компании: '))
isderzki = int(input('Введите значение издержек компании: '))
pribil_ubitoc = viruchka - isderzki
if pribil_ubitoc > 0:
    rentabelnost = round(pribil_ubitoc / viruchka * 100, 2)
    print('Ваша компания работает с привылью в ', pribil_ubitoc, '.', 'Рентабельность: ', rentabelnost, '%')
    coll_sotr = int(input('Введите колличество сотрудников компании: '))
    pribil_sotr = round(pribil_ubitoc / coll_sotr, 2)
    print('Прибыль на одного сотрудника составила: ', pribil_sotr)
else:
    print('Убыток вашей компании составил: ', pribil_ubitoc)
