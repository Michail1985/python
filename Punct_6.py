my_dict = dict()
with open('file_name6.txt', encoding='utf-8') as my_file:
    for line in my_file.readlines():
        name = line.split()
        predmet = name[0]
        new_chis = 0
        for chislo in name[1:]:
            buk = ''
            new_chislo = ''
            try:
                for buk in chislo:
                    try:
                        if int(buk) in range(9):
                            new_chislo = new_chislo + buk
                    except ValueError:
                        continue
                new_chislo = int(new_chislo)
            except ValueError:
                continue
            #print(new_chislo)
            new_chis = new_chis + int(new_chislo)
        my_dict[predmet[:-1]] = new_chis
    print(my_dict)