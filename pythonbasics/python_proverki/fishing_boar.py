budget = int(input())
season = input()
number = int(input())
boat_rent = 0

if season == 'Spring':
    boat_rent = 3000

elif season == 'Winter':
    boat_rent = 2600
else:
    boat_rent = 4200

if number <= 6:
    boat_rent *= 0.9
elif number <= 11:
    boat_rent *= 0.85
elif number >= 12:
    boat_rent *= 0.75

if season != 'Autumn' and number % 2 == 0:
    boat_rent *= 0.95
difference = abs(boat_rent - budget)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

