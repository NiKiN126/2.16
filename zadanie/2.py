#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four'
    }
    new_words = dict(zip(words.values(), words.keys()))
    print(new_words)
