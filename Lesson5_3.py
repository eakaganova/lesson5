# Создать текстовый файл (не программно)
import math
with open('file_for_lesson5_ex_3.txt', 'w+') as my_file:
    lastname_pay = {'Ivanov': 10, 'Petrov': 40, 'Alekseeva': 500, 'Martova': 150}
# построчно записать фамилии сотрудников и величину их окладов
    for key, value in lastname_pay.items():
        my_file.write(f'{key} получает {value} т.р.\n')
        if value > 20:
            print(f'Больше 20 т.р. получает: {key}')
# Выполнить подсчет средней величины дохода сотрудников.
count_pay = [value for key, value in lastname_pay.items()]
average_pay = sum(count_pay) / len(count_pay)
print(f'Средняя зарплата составляет {average_pay}')
