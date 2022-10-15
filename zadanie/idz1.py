#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    humans = []
    print('Список комманд: \n exit \n add \n list \n select')
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 15,
        '-' * 16
    )
    while True:
        com = input('Введите команду: ').lower()
        if com == 'exit':
            break
        elif com == "add":
            name = input('Введите Ф.И.О.: ')
            zodiac = input('Введите знак зодиака: ')
            daytime = input('Введите дату рождения: ')
            day = daytime.find("/")
            month = daytime.find("/")
            year = daytime.find("/")
            human = {
                'name': name,
                'zodiac': zodiac,
                'daytime': daytime

            }
            humans.append(human)
            if len(humans) > 1:
                humans.sort(key=lambda x: x.get('daytime', ''))
        elif com == 'list':
            print(line)
            print(
                '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Знак Зодиака",
                    "Дата рождения"))
            print(line)
            for idx, human in enumerate(humans, 1):
                print(
                    '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                        idx,
                        human.get('name', ''),
                        human.get('zodiac', ''),
                        human.get('daytime', 0)
                    )
                )
            print(line)
        elif com == 'select':
            nom = input('Введите дату рождения: ')
            count = 0
            print(line)
            print(
                '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Знак Зодиака",
                    "Дата рождения"))
            print(line)
            for i, num in enumerate(humans, 1):
                if nom == num.get('daytime', ''):
                    count += 1
                    print(
                        '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                            count,
                            num.get('name', ''),
                            num.get('zodiac', ''),
                            num.get('daytime', 0)))
            print(line)
            if count == 0:
                print('Таких людей нет')
        else:
            print(f"Неизвестная команда {com}", file=sys.stderr)
