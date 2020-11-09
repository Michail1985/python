my_file = open('file_name2.txt')
counts = 0
while True:
    content = my_file.readline()
    if content == '':
        break
    else:
        counts += 1
        slovo = len(content.split())
        print(f'Строка {counts}: колличество слов - {slovo}')
my_file.close()
print(f'Колличество строк: {counts}')