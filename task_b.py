from math import pi
x = 0.50
print("________________________________")
print("|", "x", "\t        |", "y", "            |")
print("|_______________|_______________|")
while x <= 0.95:
    sum = 0
    n = 1
    while True:
        f = (pi / 2) - x - ((((2 * n) - 1) / ((2 * n) * (2 * n + 1))) * x ** ((2 * n) + 1))
        sum += f
        if abs(f) > 0.001:
            break
        n += 1
    print("|", "x =", round(x, 3), "\t|", "y =", round(sum, 4), "\t|")
    x += 0.05
print("|_______________|_______________|")