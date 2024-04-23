en_ru_dict = {}
# with open () авто закрытие после завершения работы с файлом
with open("en-ru.txt") as file:
    for line in file:
        line = line.strip() # удаляются пробелы и символы новой строки с начала и конца текущей строки
        en_word, ru_translations = line.split(' - ')
        ru_words = ru_translations.split(', ')
        for ru_word in ru_words:
            if ru_word in en_ru_dict:
                en_ru_dict[ru_word].append(en_word)
            else:
                en_ru_dict[ru_word] = [en_word] # создание новой записи рус-ключ англ- значение

with open('ru-en.txt', 'w') as file: # pежим 'w' открытие файла на запись
    for ru_word in sorted(en_ru_dict.keys()):
        en_translations = ', '.join(sorted(en_ru_dict[ru_word]))  # join - объединение
        file.write(f"{ru_word} - {en_translations}\n") # переход строки