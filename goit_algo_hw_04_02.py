from pathlib import Path

def get_cats_info(path):

    with open(path, 'r', encoding="utf-8") as file:
        cats_info = []
        line_number = 0  # Змінна для відстеження номера рядка
            
        for line in file:

            cat_info = {}
            cat = line.strip().split(',')
            line_number += 1
            cat_info['id'] = cat[0]
            cat_info['name'] = cat[1]
            cat_info['age']= cat[2]
            cats_info.append(cat_info)
    return cats_info

print(get_cats_info('cats_file.txt'))