x = int(input("Podaj współżędną X: "))
y = int(input("Podaj współżędną Y: "))
if (x > 100 and y > 100) or (x < 0 and y < 0):
    print("Gracz jest poza planszą.")
else:
    if x <= 10 and y <= 10:
        p = "w lewym dolnym rogu."
    elif x > 10 and x <= 90 and y <= 10:
        p = "na dolnej krawędzi."
    elif x > 90 and y <= 10:
        p = "w prawym dolnym rogu."
    elif x <= 10 and y > 10 and y <= 90:
        p = "na lewej krawędzi."
    elif x > 90 and y > 10 and y <= 90:
        p = "na prawej krawędzi."
    elif x <= 10 and y > 90:
        p = "w lewym górnym rogu."
    elif x > 10 and x <= 90 and y > 90:
        p = "na górnej krawędzi."
    elif x > 90 and y > 90:
        p = "w prawym górnym rogu."
    else:
        p = "w pozycji centralnej."

        print(f"Gracz znajduje się {p}")
