#!/usr/bin/env python3

file = open('numbers.txt', 'r') 

integers = []
for str in file.readlines():
    integers.append(int(str))
    print(integers)
for numbers in integers:
    for numbers2 in integers:
        if numbers + numbers2 == 2020:
            print("Answer: ",numbers * numbers2)
            exit()
