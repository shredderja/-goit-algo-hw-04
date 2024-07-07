from pathlib import Path

def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(',')
                    cats_info.append({
                        'id': cat_id,
                        'name': name,
                        'age': int(age)
                    })
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
    
    return cats_info

path_to_file = Path('homework4-2/cats.txt')
cats = get_cats_info(path_to_file)

for cat in cats:
    print(cat)