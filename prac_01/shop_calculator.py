DISCOUNT = 0.9
number = int(input("Number of items: "))
total_price = 0
for i in range(number):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    discount_total_price = DISCOUNT * total_price
    print("Total price for {} items is ${:.2f}".format(number, discount_total_price))