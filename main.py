def create_dict_from_file(path):
    recept = {}
    f = open(path, 'r', encoding='utf-8')

    dish = f.readline().replace('\n', '')
    print(dish)
    recept[dish] = []
    ing = {}
    ing_line = []
    line = f.readline()
    while line:
        ing = {}
        if line == '\n':
            line = f.readline()
            dish = line.replace('\n', '')
            recept[dish] = []
        elif line.find(' | ') != -1:
            ing_line = line.split(' | ')
            ing['ingredient name'] = ing_line[0]
            ing['quantity'] = ing_line[1]
            ing['measure'] = ing_line[2]
            recept[dish].append(ing)
            line = f.readline()
        else:
            line = f.readline()

    f.close()
    return recept

cook_book = create_dict_from_file('recepies.txt')
print(cook_book['Фахитос'])
