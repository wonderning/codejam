#!/usr/bin/env python
import itertools
item_list, sum_list = [], []
item_total = int(input())
for i in range(item_total):
    str_tmp = input()
    item_list.append([int(i) for i in str_tmp.split()])
all_seq = itertools.permutations(list(range(item_total)))
for i in all_seq:
    total_gain = 0
    for j in range(0, len(i), 2):
        if j == len(i) - 1:
            break
        total_gain += item_list[i[j]][i[j + 1]]
    sum_list.append(total_gain)
print(max(sum_list))
