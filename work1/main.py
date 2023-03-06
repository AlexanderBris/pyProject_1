import os  # для работы с папками


# смотрим, что в текущей папке
list_of_names = os.listdir()
if list_of_names.__contains__("aristotle.txt"):
    print("открываю файл \"aristotle.txt\"")
else:
    print("нет файла \"aristotle.txt\"")
    exit()

# символы, заменяемые пробелом
spec_symbols = [
    '.', '!', '?', ':',
    ';', '\'', '\"', ',',
    '\n', '\r'
]
# список знаков препинания
spec_marks = [
    '.', '!', '?', ':',
    ';', '\'', '\"', ','
]
symbol_num = 0
symbol_num_no_space = 0
symbol_num_no_marks = 0
word_num = 0
sentence_num = 0
sentence_end_marks = ['.', '!', '?']  # список знаков конца предложения
sentence_start_flag = 0


def count_something_in_line(str_line):
    global symbol_num
    global symbol_num_no_space
    global symbol_num_no_marks
    global word_num
    global spec_symbols
    global spec_marks
    # пока не конец файла, работаем со строками
    line_chars = [char for char in str_line]  # разбиваем на символы
    symbol_num += len(line_chars)
    line_chars_no_space = [c for c in line_chars if c != ' ']
    symbol_num_no_space += len(line_chars_no_space)
    line_chars_no_marks = [c for c in line_chars if not(spec_marks.__contains__(c))]
    symbol_num_no_marks += len(line_chars_no_marks)
    # заменяем знаки на пробелы
    new_line = str_line
    for c in spec_symbols:
        new_line = new_line.replace(c, " ")

    # разбиваем строку на слова пробелами
    words = new_line.split(" ")
    words_no_nums = [c for c in words if (not(c.isdigit()) and (len(c) != 0))]
    word_num += len(words_no_nums)
    return [symbol_num, symbol_num_no_space, symbol_num_no_marks, word_num]


def count_sentences_in_lines(str_line):
    global sentence_num
    global sentence_end_marks
    global sentence_start_flag

    line_chars_temp = [char for char in str_line]  # разбиваем на символы
    for ch in line_chars_temp:
        if ch.isascii() and not(ch.isdigit()) and not(sentence_end_marks.__contains__(ch)) and sentence_start_flag == 0:
            sentence_start_flag = 1
            continue
        if ch.isascii() and sentence_end_marks.__contains__(ch) and sentence_start_flag == 1:
            sentence_start_flag = 0
            sentence_num += 1
            continue


with open("aristotle.txt", "r") as file:
    for line in file:
        # считаем всякое
        result = count_something_in_line(line)
        # считаем предложения
        count_sentences_in_lines(line)

# результат
print("количество символов в файле: ", result[0])
print("количесто символов без пробелов: ", result[1])
print("количество символов без знаков препинания: ", result[2])
print("количество слов в файле: ", result[3])
print("количество предложений: ", sentence_num)

# закрываем файл
file.close()
