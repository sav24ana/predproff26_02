'''
Решение третьей задачи предпроффесионального экзамена.
По заданной дате выводит ученого в формате фамилия и инициаллы и его препарат, если учёных несколько, то вывести всех.
Отсортировать данные по столбцу с датой в порядке возрастания.
Выведите пять самых ранних препаратов.
'''
from csv import reader, writer

# Выполнение 1-й части задания
with open('scientist.txt', encoding='utf-8') as data_file:
    # Открыть файл с данными как объект reader
    csv_data = reader(data_file, delimiter='#')
    # Линейным поиском получить ответ
    for row in csv_data:
        data_admina = input()
        if data_admina in row[2]:
            print(f'Ученый {row[0]} создал препарат: {row[1]} - {row[2]}')
        else:
            print('В этот день ученые отдыхали')













from csv import reader

with open('students.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    pupil_data = list(reader(data_file, delimiter=','))
# Ввод первого значения
project_id = input('Введите номер проекта или СТОП: ')
# Цикл до ввода СТОП
while project_id != 'СТОП':
    # Линейный поиск позиции искомого значения
    position = -1
    for i in range(len(pupil_data)):
        if pupil_data[i][2] == project_id:
            position = i
            break
    # Вывод на экран
    if position >= 0:
        pupil_name = pupil_data[position][1].split()
        name = pupil_name[1][0] + '.' + pupil_name[0]
        print(f'Проект No {project_id} делал: {name} он(а) получил(а) оценку - {pupil_data[position][4]}.')
    else:
        print('Ничего не найдено.')
    # Чтение следующего значения
    project_id = input('Введите номер проекта или СТОП: ')