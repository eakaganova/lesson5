# Создать текстовый файл (не программно),
with open('file_for_lesson5_ex2.txt', 'r+') as my_file:
    # сохранить в нем несколько строк
    while True:
        user_text = input('Введите несколько строк: ')
        my_file.write(user_text + '\n')
        if user_text == '':
            break
    # выполнить подсчет количества строк
    line_count = my_file.readlines()
    print(f'Количество строк: {len(line_count)}')
    # количества слов в каждой строке
    i = 0
    for line in line_count:
        i += 1
        word_count = line.split()
        print(f'Количество cлов в строке {i}: {len(word_count)}')
