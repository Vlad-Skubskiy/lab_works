#Створіть змінну `movie` та присвойте їй назву вашого улюбленого фільму. Виведіть рядок, який містить назву фільму.              
movie = "Bad boys"
print(movie)

#Створіть змінну `is_employee` та присвойте їй значення `True`, а змінну `is_employer` - значення `False`. Виведіть результати логічних операцій.
is_employee = True
is_employer = False
print(is_employee and is_employer)

#Створіть змінну `is_sunny` та присвойте їй значення `False`, а змінну `is_raining` - значення `True`. Виведіть результати логічного "не".      
is_sunny = False
is_raining = True

print(not is_sunny)
print(not is_raining)

#math
import math

x=2.531
y=0.193
result = y * ((x * y) ** (1 / 3)) + y * math.sin(x * y) - ((math.e) ** ((-x) * y)) * math.cos(x * y) + 7.1/ (x * y)
print(result)
