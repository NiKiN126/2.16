#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список людей.
    humans = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Фамилия и инициалы? ")
            zodiac = input("Знак Зодиака? ")
            Birthdate = list(map(int, input("Дата рождения? ").split()))
            # Создать словарь.
            human = {
                'name': name,
                'zodiac': zodiac,
                'Birthdate': Birthdate,
            }
            # Добавить словарь в список.
            humans.append(human)
            # Отсортировать список в случае необходимости.
            if len(humans) > 1:
                humans.sort(key=lambda x: x.get('Birthdate')[::-1])

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Знак Зодиака",
                    "Дата рождения"
                )
            )
            print(line)

            # Вывести данные о всех людях.
            for idx, human in enumerate(humans, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        human['name'],
                        human['zodiac'],
                        # переводим дату рождения в строку
                        ' '.join((str(i) for i in human['Birthdate']))
                    )
                )
            print(line)
        elif command == 'whois':

            who = input('Кого ищем?: ')
            flag = 0
            for human in humans:
                if who in human:
                    flag = 1
            if not flag:
                print('Не найдено')
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("whois - вывести нужного работника;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print('Неизвестная команда', command, file=sys.stderr)
