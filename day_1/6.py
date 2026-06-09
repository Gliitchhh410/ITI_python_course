n = int(input('Enter the depth of the pyramid(integer): '))

j = 0
for i in range(n):
    for j in range(i):
        print('*', end = '')
    print()
    j = 0

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end = '')
    print()
    j = 0