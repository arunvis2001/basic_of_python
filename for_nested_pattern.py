row = range(1, 11, 2)
for i in range(12):
    for col in row:
        count = ''
        for item in range(col):
            count += 'X'
        print(count)
    if i % 2 == 0:
        row = range(11, 2, -2)
    else:
        row = range(1, 11, 2)

