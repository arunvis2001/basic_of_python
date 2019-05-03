itr = 1
unit = int(input('Enter a number less than 5 : '))
while itr <= unit:
    print(f'Iteration : {itr}')
    itr += 1
    if unit >5:
        print('Number is greater than 5')
        break
else:
    print('Done')