with open('day1.txt', 'r') as file:
    n = [int(x) for x in file.readlines()]
n.sort()
fix, min, max = (0, 1, len(n)-1)
while n[fix] + n[min] + n[max] != 2020:
    min,max = (fix+1, len(n) - 1)
    while n[fix] + n[min] + n[max] != 2020:
        if n[fix] + n[min] + n[max] < 2020:
            min += 1
        if n[fix] + n[min] + n[max] > 2020:
            max -= 1
print(n[fix], n[min], n[max], n[fix] * n[min] * n[max])
