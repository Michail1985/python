with open('file_name4.txt', encoding='utf-8') as my_file:
    with open('file_rus.txt', 'w', encoding='utf-8') as my_rus:
        for line in my_file.readlines():
            count, count_2 = line.split(' - ')
            if count == 'One':
                line = line.replace('One', 'Один')
            elif count == 'Two':
                line = line.replace('Two', 'Два')
            elif count == 'Three':
                line = line.replace('Three', 'Три')
            elif count == 'Four':
                line = line.replace('Four', 'Четыре')
            my_rus.write(line)