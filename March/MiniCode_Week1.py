import re
num, string = input(), input()
if re.match(r'^("[a-zA-Z\d]{1,50}",){0,49}"[a-zA-Z\d]{1,50}"$', string) and num.isdigit() and 2 <= int(num) <= 10:
    child_get, total_remain, dict, num, str = 0, 0, {}, int(num), re.sub('[,"]', "", string)
    for letter in str: dict[letter] = dict[letter] + 1 if letter in dict else 1
    for letter in dict: child_get, total_remain = child_get + dict[letter] // num, total_remain + dict[letter] % num
    print('%d,%d' % (child_get, total_remain))
else: print("-1,-1")
