limit = 1000000000000
n = 0
summe = 0

while summe <= limit:
    n += 1
    summe += n

print(n)
print(str(summe)[-2:])