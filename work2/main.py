import csv
import os  # для работы с папками
import sys

# смотрим, что в текущей папке
list_of_names = os.listdir()
if list_of_names.__contains__("steam.csv"):
    print("открываю файл \"steam.csv\"")
else:
    print("нет файла \"steam.csv\"")
    exit()
# открываем файл
file = open("steam.csv", 'r', encoding='utf-8-sig')
# with open("steam.csv", "r") as file:
row = csv.reader(file, delimiter=',', quotechar=';')
# берем первую строку
question_word_list = row.__next__()
# убираем лишнее
question_word_list = question_word_list[4:-7]

# множество предпочитаемых сущностей
prefer_variants = set()
# задаем вопросы и заполняем множество предпочитаемых сущностей
for cat in question_word_list:
    print("What", cat, "you prefer?")
    val = {w.lower() for w in input().split(' ')}  # делаем все нижним регистром
    prefer_variants = prefer_variants | val  # объединяем с новыми данными
# удаляем пустой вариант
prefer_variants.discard('')

games_dict = {}
for word_list in row:
    game_variants = set(word_list[2::])
    # приводим все имена к нижнему регистру
    game_variants = {words.lower() for words in game_variants}
    # формируем словарь {'имя игры' : {множество слов}}
    games_dict.update({word_list[1]: game_variants})

with open('result.txt', 'w', encoding='utf-8-sig') as f:
    sys.stdout = f
    print("игра с наибольшим  баллом наиболее подходит")
    print("игра ----> балл")
    for word_list in games_dict:
        # создаем множество из пересечения множеств (набор общих элементов)
        eq_vals = games_dict[word_list] & prefer_variants
        # пишем в файл
        print(word_list, "---->", len(eq_vals))

file.close()
