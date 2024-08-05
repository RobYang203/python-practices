a = 10

while a >= 0:
    print('now a=', a)
    a -= 1

    if a == 2:
        break


for i in range(10):
    print('for loop now i=', i)

for i in range(10, 0, -1):
    print("for loop desc now i=", i)

list_a = list(range(10))

for i in list_a:
    print('list for loop now i=', i)


for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        end = ''
        if j == 9:
            end = '\n'

        print(f'{i} * {j} = {i*j:2d} | ', end=end)
