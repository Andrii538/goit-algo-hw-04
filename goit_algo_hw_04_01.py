from pathlib import Path

def total_salary(path):
    """
    Розраховує розмір загальної і середньої заробітної плати.\n
    Аргумент:
    path: Шлях до файлу з даними про заробітню плату. 
    Формат даних: прізвище розробника та його заробітня плата, які розділені комою без пробілів.\n
    Повертає:
    Кортеж елементами якого є: загальна заробітня плата і середня заробітня плата.\n
    """
    try:
        with open(path, 'r', encoding="utf-8") as file:
            total = 0           # Змінна для підрахунку загальної зп
            line_number = 0     # Змінна для відстеження номера рядка
            try:
                for line in file.readlines():
                    line_number += 1
                    salary = line.split(',')    # Розділяємо рядок за комою
                    total += int(salary[1])     
                average = total / line_number   # Розраховуємо середню зп
            except IndexError:
                return f'Помилка при обробці рядка - {line_number}'
            # Повторно використовуємо номер рядка, для відстеження помилки в ньому
        return (total, round(average))
    # Опрацьовуємо можливі помилки
    except FileNotFoundError:
        return 'Файл не знайдено'
    
    except ZeroDivisionError:
        return 'Файл порожній або не містить даних про заробітню плату'
    
    except ValueError:
        return 'Не правильний формат вхідних даних' 

if __name__ == "__main__":

    total, average = total_salary("goit_algo_hw_04_01_data.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")