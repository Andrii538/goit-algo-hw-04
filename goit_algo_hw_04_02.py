from pathlib import Path

def get_cats_info(path):
    """
    Опрацьовує файл з даними про котів і повертає список словників з інформацією про кожного кота.\n
    Аргумент:
    path: Шлях до файлу з даними про котів. 
    Формат даних: рядок який містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.\n
    Повертає:
    Список словників з інформацією про кожного кота.\n
    """
    try:
        # Перевіряємо чи файл непорожній
        file_path = Path(path)
        if file_path.stat().st_size == 0:
            return 'Файл порожній'
        
        with open(path, 'r', encoding="utf-8") as file:
            cats_info = []      # Створюємо порожній список
            line_number = 0     # Змінна для відстеження номера рядка і повідомлення про помилку в конкретному рядку
            try: 
                for line in file:

                    cat_info = {}
                    cat = line.strip().split(',')   # Розділяємо рядок з інфорацією за комою
                    line_number += 1
                    cat_info['id'] = cat[0]
                    cat_info['name'] = cat[1]
                    cat_info['age']= cat[2]
                    # Перевіряємо чи всі дані про кота були занесені у файл
                    if cat[0] == "":
                        return f'Відсутній ідентифікатор кота в рядку {line_number}'
                    if cat[1] == "":
                        return f"Відсутнє ім'я кота в рядку {line_number}"
                    if cat[2] == "":
                        return f'Відсутній вік кота в рядку {line_number}'
                    cats_info.append(cat_info)
                return cats_info
            
            except IndexError:      # У разі, якщо якийсь з рядків порожній
                return f'Помилка при обробці рядка - {line_number}'
            
    except FileNotFoundError:
        return 'Файл не знайдено'

# Приклад використання
cats_info = get_cats_info('cats_file.txt')
for cat in cats_info:
        print(cat)
