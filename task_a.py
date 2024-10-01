import math

print("________________________")
print("|", "  x  ", " |", "\t y", "     |")
print("|________|______________|")
x = 2.0
while x <=5:
    if x < 3:
        result = math.cos(x + 1 / math.sin(x ** (-2))) / math.sin(x + 1 / math.sin(x ** (-2)))        
    elif 3 <= x <= 4 : 
        result = math.log10(math.log(x) + math.log(x, 3))     
    else:
        result = math.cos(5 * (x ** 2))
    print("|x =", round(x, 3), "|", "y =", round(result, 4), "\t|")
    x += 0.2