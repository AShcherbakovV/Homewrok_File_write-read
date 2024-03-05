def create_dict_from_file(path):
    recept = {}
    f = open(path, 'r', encoding='utf-8')

    dish = f.readline().replace('\n', '')
    print(dish)
    recept[dish] = []
    ing_line = []
    line = f.readline()
    while line:
        if line == '\n':
            line = f.readline()
            dish = line.replace('\n', '')
            recept[dish] = []
        elif line.find(' | ') != -1:
            ing_line = line.split(' | ')
            recept[dish].append({'ingredient name': ing_line[0], 'quantity': int(ing_line[1]), 'measure': ing_line[2]})#Добавил преобразование в числовой формат, для более комфортной обработки итогового словаря в функции shoplist_create()
                                                                                                                       # и избавился от буферного словаря ingr. Можно посмотреть в предыдущей версии
            line = f.readline()
        else:
            line = f.readline()

    f.close()
    return recept

def shoplist_create(dishes: list, persons: int, cookbook): #В условии задачи было сказано об использовании только двух входных параметров функции,
                                                           # но я добавил cook_book(книга рецептов) дабы избавиться от использованияглобальной перменной
    shop_list = {}
    for dish in dishes:
        for ingr in cookbook[dish]:
            if shop_list.get(ingr['ingredient name']) == None:
                shop_list[ingr['ingredient name']] = {'measure': ingr.get('measure'), 'quantity': int(ingr.get('quantity')) * persons}
            else:
                shop_list[ingr['ingredient name']]['quantity'] = shop_list[ingr['ingredient name']]['quantity'] + ingr.get('quantity') * persons
    return shop_list

def file_from_files(path_list): #Функция слияния файлов
    list_cort = []
    file_list = []
    for path_file in path_list:
        f = open(path_file, 'r', encoding='utf-8')
        file_list = f.readlines()
        for elem in file_list:
            elem.replace('\n', '')
        list_cort.append((path_file, len(file_list), file_list))
        f.close()

    list_cort = sorted(list_cort, key=lambda x: x[1])
    f = open('file from files.txt', 'w', encoding='utf-8')
    for cort in list_cort:
        f.write(cort[0] + '\n')
        f.write(str(cort[1]) + '\n')
        for line in cort[2]:
            if line.find('\n') == -1:
                f.write(line + '\n')
            else:
                f.write(line)
    f.close()
    return

cook_book = create_dict_from_file('recepies.txt')

print(cook_book['Фахитос'])
print(shoplist_create(['Омлет', 'Фахитос'], 3, cook_book))

file_from_files(['2.txt', '1.txt'])
