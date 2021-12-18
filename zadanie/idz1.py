#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Список работников.
    workers = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Фамилия и инициалы? ")
            zodiac = input("Знак Зодиака? ")
            year = list(map(int, input("Дата рождения? ").split()))
            # Создать словарь.
            worker = {
                'name': name,
                'zodiac': zodiac,
                'year': year,
            }
            # Добавить словарь в список.
            workers.append(worker)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                # сортировка -> нужно, чтобы 22 1 2000 раньше 1 2 2000
                # workers.sort(key=lambda x : x.get('year') -> тут сортировка
                # по первому элементу, затем по второму и тд. Поэтому:
                workers.sort(key=lambda x: x.get('year')[::-1])

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

            # Вывести данные о всех сотрудниках.
            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        worker['name'],
                        worker['zodiac'],
                        # переводим дату рождения в строку
                        ' '.join((str(i) for i in worker['year']))
                    )
                )
            print(line)
        elif command == 'whois':

            who = input('Кого ищем?: ')
            flag = 0
            for worker in workers:
                if who in worker:
                    flag = 1
                    info(workers, who)

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