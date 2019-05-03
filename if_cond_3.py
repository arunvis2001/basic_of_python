weight = int(input('Enter your Weight : '))
unit = input('(L)bs or (K)g : ').upper()
if unit == "L":
    weight *= 0.45
    print(f"Weight in Kg : {weight}")
elif unit == 'K':
    weight /= 0.45
    print(f"Weight in Lbs : {weight}")
else:
    print('Its not right key')