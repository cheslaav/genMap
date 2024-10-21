import random
import json
from random import uniform, randint
from xml.etree.ElementTree import tostring

from faker import Faker

fake = Faker('ru_RU')

stories_count = 40000

# Исходный JSON-файл
with open('input.json', 'r') as f:
    data = json.load(f)

# Обновляем секцию stores
data['stores'] += [{
    'address': fake.street_address(),
    'allAvailable': random.choice([True, False]),
    'availableCount': random.randint(0, 1),
    'basket': [{"available": random.choice([True, False]), "goodID": f"700{random.randint(0, 9999999)}"}],
    'code': f"900{random.randint(0, 9999999)}",
    'coordinates': {
        'x': round(random.uniform(36.0000, 37.9999), 4),
        'y': round(random.uniform(54.0000, 55.9999), 4)
    },
    'name': 'Аптека ' + fake.company(),
    'retailBrand': 'Магнит Аптека ' + fake.first_name(),
    'working_hours_description': f"C {randint(5, 23)}:00 до {randint(22, 23)}:00"
} for i in range(stories_count)]

# Записываем обновлённый JSON-файл
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Чтение файла
with open('output.json', 'r') as f:
    data = json.load(f)

# Хранение всех пар координат в множестве
unique_coords = set()
for store in data['stores']:
    coords = (store['coordinates']['x'], store['coordinates']['y'])
    if coords in unique_coords:
        print("Дублирование координат:", coords)
        # Удаление элемента из списка stores
        index = data['stores'].index(store)
        del data['stores'][index]
        print("Дубли координат удалены")
    else:
        unique_coords.add(coords)


total_count = len(data["stores"])
# Вывод количества элементов
print(len(data["stores"]))

# Запись данных обратно в файл
with open('unic'+str(total_count)+'.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)