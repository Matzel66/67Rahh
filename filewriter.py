i=1
with open("daten.txt" , "a") as f:
    while i <= 10000:
        i += 1
        wert= (i*i+17*i+23) % 1000
        f.write(str(wert) + "\n")