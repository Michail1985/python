import json

firm_dict = {}
sredn = 0
i=0
with open('file_name7.txt', encoding='utf-8') as my_file:
    for line in my_file.readlines():
        name, forma, dovod, rashod = line.split()
        itog = int(dovod) - int(rashod)
        firm_dict[name] = itog
        if itog > 0:
            i += 1
            sredn = round((sredn + itog)/i, 2)
    info = [firm_dict, {'Средняя прибыль компаний': sredn}]

with open('file_name.json', 'w', encoding='utf-8') as json_file:
    json.dump(info, json_file)

with open('file_name.json', encoding='utf-8') as json_file:
    print(json.load(json_file))