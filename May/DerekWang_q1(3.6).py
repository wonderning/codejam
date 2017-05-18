#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Compiled and executed in python 3.

(v1, v2) = input().split(" ")
v1_split = [int(i) for i in v1.split(".")]
v2_split = [int(i) for i in v2.split(".")]
# make two array equally long by adding 0 to the shorter one.
len1, len2 = len(v1_split), len(v2_split)

if len1 > len2:
    for i in range(len1 - len2):
        v2_split.append(0)
else:
    for i in range(len2 - len1):
        v1_split.append(0)

result = 0
for i in range(len(v1_split)):
    if v1_split[i] > v2_split[i]:
        result = 1
        break
    elif v1_split[i] < v2_split[i]:
        result = -1
        break

print(result)
