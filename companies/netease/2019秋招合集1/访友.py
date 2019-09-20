x = int(input())

steps = [1, 2, 3, 4, 5]

c = 0
while x:
    if x < steps[-1]:
        steps.pop()
        continue
    x -= steps[-1]
    c += 1
print(c)