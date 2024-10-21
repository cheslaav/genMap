import json
from random import uniform, randint

count = 2

def generate_store():
    def generate_random_coordinate():
        x = uniform(37.0000, 37.9999)
        y = uniform(55.0000, 55.9999)
        return {"x": round(x, 4), "y": round(y, 4)}

    # Генерация всех необходимых свойств
    address = f"г. Москва, ул. Велозаводская, д. {randint(1, count)}/{randint(1, count)}"
    all_available = bool(randint(0, 1))
    available_count = randint(0, 1)
    basket = [{
        "available": bool(randint(0, 1)),
        "goodID": f"700{randint(0, 9999999)}"
    }]
    code = f"900{randint(0, 9999999)}"
    coordinates = generate_random_coordinate()
    name = f"Аптека {randint(1, count)}"
    retail_brand = f"Магнит Аптека {randint(1, count)}"
    working_hours_description = f"C {randint(5, 23)}:00 до {randint(22, 23)}:00"

    return {
        "address": address,
        "allAvailable": all_available,
        "availableCount": available_count,
        "basket": basket,
        "code": code,
        "coordinates": coordinates,
        "name": name,
        "retailBrand": retail_brand,
        "working_hours_description": working_hours_description
    }

def create_structure(num_stores=count):
    structure = {
        "items": {
            "1000316386": {
                "goodID": "1000316386",
                "image": {
                    "defaultSize": "416x416",
                    "postfixUrl": "/uf/a57/a573f258ae2345546f3d3306211112a0/f1efe003811889d353fdd19ecc515a54.jpeg",
                    "prefixUrl": "https://img-dostavka.magnit.ru/resize/"
                },
                "name": "Парацетамол таблетки 500мг 20шт"
            },
            "7000000859": {
                "goodID": "7000000859",
                "image": {
                    "defaultSize": "416x416",
                    "postfixUrl": "/uf/1c3/1c31776c279c5bc253735fe4ebfa3b04/13a07c4b4e5f534ea745bca2c2debdfd.jpeg",
                    "prefixUrl": "https://img-dostavka.magnit.ru/resize/"
                },
                "name": "Пенталгин таблетки 12шт"
            }
        },
        "stores": [],
        "totalItemsCount": 2
    }

    for _ in range(num_stores):
        store = generate_store()
        structure["stores"].append(store)

    return structure

if __name__ == "__main__":
    output_struct = create_structure()
    with open("output32k.json", "w") as outfile:
        json.dump(output_struct, outfile, ensure_ascii=False)

    print("Структура данных успешно создана и сохранена в файл output32k.json.")