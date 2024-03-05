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

cook_book = create_dict_from_file('recepies.txt')
print(cook_book['Фахитос'])
print(shoplist_create(['Омлет', 'Фахитос'], 3, cook_book))
