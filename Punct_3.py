with open('file_name3.txt', encoding='utf-8') as my_file:
    dohods = []
    for line in my_file.readlines():
        name, dohod = line.split()
        dohods.append(float(dohod))
        if float(dohod) < 20000:
            print(name)
    print('Средняя заработная плата:', round(sum(dohods) / len(dohods), 2))