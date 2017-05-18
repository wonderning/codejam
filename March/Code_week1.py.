#!/usr/bin/env python
# -*- coding: utf-8
# Author: Derek Wang
# This is verified in Python 3.6.

import re

# limit of total children
COUNT_LIST = [i for i in range(2, 11)]
# Regular expression for string input
PAT = r'^("[a-zA-Z\d]{1,50}",){0,49}"[a-zA-Z\d]{1,50}"$'


def string2count(string, num):
    num = int(num)
    (child_get, total_remain, dict) = (0, 0, {})
    string_list = re.sub('[,"]', "", string)
    for letter in string_list:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    for letter in dict:
        child_get += dict[letter] // num
        total_remain += dict[letter] % num
    print('%d,%d' % (child_get, total_remain))


if __name__ == '__main__':
    child_count = input()
    new_string = input()
    if re.match(PAT, new_string) and child_count.isdigit() and int(child_count) in COUNT_LIST:
        string2count(new_string, child_count)
    else:
        print("-1,-1")
