budget_petar = float(input())
number_videocard = int(input())
number_procesor = int(input())
number_ram_memmory = int(input())

videocard_price = 250
processor = videocard_price * 0.35
ram_memmory = videocard_price * 0.1
discount = 0


sum_videocard = number_videocard * videocard_price
price_processors = sum_videocard * 0.35
sum_procesor = number_procesor * price_processors
price_ram = sum_videocard * 0.1
sum_ram = number_ram_memmory * price_ram
total_sum = sum_videocard + sum_procesor + sum_ram

if number_videocard > number_procesor:
    total_sum *= 0.85

if budget_petar >= total_sum:
    print(f"You have {budget_petar - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum- budget_petar:.2f} leva more!")


