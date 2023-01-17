sojourn = int(input()) - 1
room = input()
rate = input()
price = 0
if room == 'room for one person':
    price = 18
elif room == 'apartment':
    price = 25
    if sojourn > 15:
        price *= 0.50
    elif sojourn >= 10:
        price *= 0.65
    else:
        price *= 0.70
elif room == 'president apartment':
    price = 35
    if sojourn > 15:
        price *= 0.8
    elif sojourn >= 10:
        price *= 0.85
    else:
        price *= 0.9

if rate == 'positive':
    price *= 1.25
elif rate == 'negative':
    price *= 0.9

total_price = price * sojourn

print(f"{total_price:.2f}")




