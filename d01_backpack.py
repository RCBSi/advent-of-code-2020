with open('day1.txt', 'r') as file:
    _input = [int(x) for x in file.readlines()]
_input.sort()
min = 0
max = len(_input) - 1
while _input[min] + _input[max] != 2020:
    if _input[min] + _input[max] < 2020:
        min += 1
    if _input[min] + _input[max] > 2020:
        max -= 1
print(_input[min], _input[max], _input[min]*_input[max])
