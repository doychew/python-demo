degrees = int(input())
time = input()
Outfit =''
Shoes =''
if time == 'Morning':
    if 10 <= degrees <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
elif time == 'Morning':
    if 18 < degrees <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
elif time == 'Morning':
    if degrees >= 25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'

if time == 'Afternoon':
    if 10 <= degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    else:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
if time == 'Evening':
    if 10 <= degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif degrees >= 25:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'


print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

