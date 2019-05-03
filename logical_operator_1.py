credit = False
income = 0
if credit and income:
    print('Congrats your loan is approved')
elif credit or income:
    print('Reach to nearest branch')
else:
    print('Sorry your loan is not approved')
print('Thank you')
