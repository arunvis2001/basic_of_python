price = 100000
credit = False
if credit:
    dp = price * 0.1
    print(f"Down Payment is ${dp}")
else:
    dp = price * 0.2
    print(f"Down Payment is ${dp}")
print(f"House Price is ${price}")