# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение

russian_dict = {'One': 'Один',
                'Two': 'Два',
                'Three': 'Три',
                'Four': 'Четыре'}

with open('file_for_lesson5_ex_4.txt') as my_file_4, open('new_file5_4.txt', 'w+') as new_file_54:
    # считывающую построчно данные.
    text_5 = my_file_4.readlines()
    for line in text_5:
        key, value = line.rstrip().split(' — ')
# При этом английские числительные должны заменяться на русские.
        new_file_54.write(f'{russian_dict[key]} - {value}\n')
# Новый блок строк должен записываться в новый текстовый файл.


