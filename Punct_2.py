def my_func(**kwargs):
    return kwargs
print(my_func(name=input('Имя: '), surname=input('Фамиия: '),
    god=input('Год рождения: '), city=input('Город проживания: '),
    email=input('email: '), phone=input('Телефон: ')))