House_price=1000000
Have_gc=True
#Have_gc=True

if Have_gc:
    down_payment = 0.1 * House_price
else:
    down_payment = 0.2 * House_price
print(f"Down payment: {down_payment}")
