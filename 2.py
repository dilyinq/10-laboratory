import json

with open(r"10.1.json") as file:
    a = json.load(file)

new_product = {}
new_product['name'] = input("Введите название продукта: ")
new_product['price'] = int(input("Введите цену продукта: ")) # преобразование в целое число
new_product['available'] = input("Продукт доступен? (yes/no): ").lower() == 'yes'
new_product['weight'] = int(input("Введите вес продукта: "))

# Добавление нового продукта в список
a['products'].append(new_product)

# Запись обновленных данных в файл
with open('products.json', 'w') as file:
    json.dump(a, file, indent=4)
