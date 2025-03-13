# from pathlib import Path
# import re

# def total_salary(path):
#     try:
#         with open(path, 'r', encoding="utf-8") as file:
#             total_len = sum(1 for _ in file)
#             file.seek(0)
#             total = 0
#             for line in file.readlines():
#                 salary = re.sub(r'[^0-9]', '', line)
#                 total += int(salary)
#             average = total / total_len
#         return tuple((total, average))
#     except (FileNotFoundError, ZeroDivisionError):
#         return 'Файл не знайдено'     

from pathlib import Path

def total_salary(path):
    
    try:
        with open(path, 'r', encoding="utf-8") as file:
            total = 0
            line_number = 0  # Змінна для відстеження номера рядка
            try:
                for line in file.readlines():
                    line_number += 1
                    salary = line.split(',')
                    total += int(salary[1])
                average = total / line_number
            except IndexError:
                return f'Помилка при обробці рядка - {line_number}'
        return (total, round(average))
    
    except FileNotFoundError:
        return 'Файл не знайдено'
    
    except ZeroDivisionError:
        return 'Файл порожній або не містить даних про заробітню плату'
    
    except ValueError:
        return 'Не правильний формат вхідних даних' 

if __name__ == "__main__":

    # total, average = total_salary("goit_algo_hw_04_01_data.txt")
    # print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    print(total_salary("goit_algo_hw_04_01_data.txt"))