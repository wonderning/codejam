#!/usr/bin/env python
person_total, input_str = int(input()), input()
person_array = [int(i) for i in input_str.split()]
infected_array, infected_array[0] = [0 for i in person_array], 1
bridge_edge, step = (0, 100), 0.5
while True:
    total_out = 0
    for i in range(person_total):
        if person_array[i] in bridge_edge:
            total_out += 1
        else:
            person_array[i] += step
    if total_out == person_total:
        break
    for i in range(person_total - 1):
        if person_array[i] not in bridge_edge:
            for j in range(i + 1, person_total):
                if person_array[i] + person_array[j] == 0:
                    person_array[i], person_array[j] = person_array[j], person_array[i]
                    infected_array[i], infected_array[j] = infected_array[i] | infected_array[j], infected_array[i] | infected_array[j]
print(sum(infected_array))
