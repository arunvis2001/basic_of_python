row = range(1, 5, 2)
for i in range(10):
    for col in row:
        count = ''
        for item in range(col):
            count += 'X'
        print(count)
    if i % 2 == 0:
        row = range(5, 0, -2)
    else:
        row = range(1, 5, 2)
