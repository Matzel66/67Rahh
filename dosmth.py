def do_something(zahl):
    if zahl < 2:
        return False
    for i in range(2, zahl):
        if zahl % i == 0:
            return False

    return True
print(do_something(7))
print(do_something(8))
print(do_something(9))