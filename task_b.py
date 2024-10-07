from math import pi
x = 0.5

print("________________________________")
print("|", "x", "\t        |", "y", "            |")
print("|_______________|_______________|")

while x <= 0.95:
    sum = (pi / 2) - x
    n = 1
    while True:             
        numerator = ((2 * n) - 1) * (x ** (2 * n + 1))
        denominator = (2 * n) * (2 * n + 1)
        f = numerator / denominator     
        if abs(f) > 0.001:
            break
        sum -= f
        n += 1
    print("|", "x =", round(x, 2), "\t|", "y =", round(sum, 4), "\t|")
    x += 0.05              #крок
    print("|_______________|_______________|")
