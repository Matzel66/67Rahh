summe = 0
for i in range(1,1001):
    if i % 4 == 0 and i % 6 != 0:
        summe += i
print(summe)