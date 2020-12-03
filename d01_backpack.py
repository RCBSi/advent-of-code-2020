with open('day1.txt', 'r') as file:
    _input = [int(x) for x in file.readlines()]
_input.sort()
min = 0
max = len(_input) - 1
while min + max != 2020:
    if min + max < 2020:
        min += 1
    if min + max > 2020:
        max -= 1
print(min, max, min*max)
