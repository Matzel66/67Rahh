def teil_a():
    summe = 0
    for i in range(1, 500001):
        if i % 7 == 0 and i % 5 != 0:
            summe += i
    return summe




def teil_b():
    summe = 0
    for i in range(1, 500001):
        if i % 11 == 0 and i % 3 != 0:
            summe += i
    return summe

print(teil_a())
print(teil_b())
print(str(teil_a() + teil_b())[-3:])