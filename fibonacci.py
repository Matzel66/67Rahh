a = 1
b = 1
stelle = 2

while len(str(b)) < 100:
    a, b = b, a + b
    stelle += 1

print(stelle)
