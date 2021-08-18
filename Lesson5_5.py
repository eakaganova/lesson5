# Создать (программно) текстовый файл,
import random
# Создать (программно) текстовый файл
with open('file_5_5.txt', 'w') as file_55:
# записать в него программно набор чисел, разделенных пробелами.
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    num_3 = random.randint(0, 100)
    num_4 = random.randint(0, 100)
    sum_num = num_1 + num_2 + num_3 + num_4
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    file_55.write(f'Суммироваться будут числа: {num_1} {num_2} {num_3} {num_4} \n')
    file_55.write(f'Сумма чисел: {sum_num}')
