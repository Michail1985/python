my_file = open('file_name.txt', 'w')
while my_file:
    content = input('Введите что-нибудь,либо нажмите Enter: ')
    if content == '':
        my_file.close()
        print('Вы прекратили вводданных.')
        break
    else:
        my_file.write(f'{content}\n')
my_file.close()