from pathlib import Path

def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
            
        total_salary = 0
        num_developers = 0
        
        for line in lines:
            surname, salary = line.strip().split(',')
            total_salary += int(salary)
            num_developers += 1
            
        if num_developers == 0:
            average_salary = 0
        else:
            average_salary = total_salary / num_developers
        
        return total_salary, average_salary
    
    except FileNotFoundError:
        print(f"Помилка: файл у  {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

path_to_file = Path('homework4-1/salaries.txt')
result = total_salary(path_to_file)
if result:
    print(f"Загальна сума зарплат: {result[0]}, Середня зарплатня: {int(result[1])}")