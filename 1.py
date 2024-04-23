import json

with open(r"10.1.json") as file:
    a = json.load(file)

# Проходимся по каждому продукту и выводим информацию на экран
for product in a ['products']:
    print('название:', product['name'])
    print('цена:', product['price'])
    print('вес:', product['weight'])
    if product['available']:
        print('в наличии')
    else:
        print('нет в наличии!')
    print()
