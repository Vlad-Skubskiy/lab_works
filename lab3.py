n = int(input('enter amount of elements:'))
list = []
for i in range(n):
    value = int(input(f'enter element {i+1}:'))
    list.append(value)
list.sort()
count = 0

for a in range (n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            if list[a] + list[b] > list[c]:
                count += 1

print(f"the amount of triangles:{count}")