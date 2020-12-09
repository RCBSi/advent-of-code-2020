with open('day09.txt', 'r') as file:
    t = [int(x.strip()) for x in file.readlines()]
x = t[min([k for k in range(25,len(t)) if max([i+j == t[k] for i in t[k-25:k] for j in t[k-25:k] if i != j]) == False])]
print('part 1', x)
y =  [t[i:j] for i in range(len(t)) for j in range(len(t)) if i < j+2 and sum(t[i:j]) == x]
print('part 2', min(y[0])+max(y[0]))
