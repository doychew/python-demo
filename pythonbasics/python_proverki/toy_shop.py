puzzle = 2.60
talking_dough = 3
toy_bear = 4.10
minion = 8.20
truck = 2

price_journey = float(input())
number_puzzle = int(input())
number_talking_dough = int(input())
number_toy_bear = int(input())
number_minion = int(input())
number_truck = int(input())

sum = (number_puzzle * puzzle) + (number_talking_dough * talking_dough) + (number_toy_bear * toy_bear)+\
      (number_minion * minion) + (number_truck * truck)
number_toys = ( number_minion + number_puzzle + number_talking_dough + number_toy_bear + number_truck)

if number_toys >= 50:
    discount = sum * 0.25
    sum -= discount

rent = sum * 0.10
profit = sum - rent
last_money = profit - price_journey
if profit >= price_journey:
    print(f"Yes! {last_money:.2f} lv left.")
else:
    print(f"Not enough money! {(last_money * -1):.2f} lv needed.")

