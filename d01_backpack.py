with open('day1.txt', 'r') as file:
    _input = [int(x) for x in file.readlines()]
_input.sort()
fix = 0
min = 1
max = len(_input) - 1
while _input[fix] + _input[min] + _input[max] != 2020:
    min = fix+1
    max = len(_input) - 1
    while _input[fix] + _input[min] + _input[max] != 2020:
        if _input[fix] + _input[min] + _input[max] < 2020:
            min += 1
        if _input[fix] + _input[min] + _input[max] > 2020:
            max -= 1
print(_input[fix], _input[min], _input[max], _input[fix] * _input[min] * _input[max])
