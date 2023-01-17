fruit = input()
day = input()
quantity = float(input())
price = 0
is_valid = True

if fruit == 'banana':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = 2.50
    elif day == 'Saturday' or day == 'Sunday':
            price=2.70
    else:
        is_valid = False
elif fruit == 'apple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = 1.20
    elif day == 'Saturday' or day == 'Sunday':
            price=1.25
    else:
        is_valid = False
elif fruit == 'orange':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = 0.85
    elif day == 'Saturday' or day == 'Sunday':
            price=0.90
    else:
        is_valid = False
elif fruit == 'grapefruit':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = 1.45
    elif day == 'Saturday' or day == 'Sunday':
            price=1.60
    else:
        is_valid = False
elif fruit == 'kiwi':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = 2.70
    elif day == 'Saturday' or day == 'Sunday':
            price=3

elif fruit == 'pineapple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = 5.50
    elif day == 'Saturday' or day == 'Sunday':
            price=5.60
    else:
        is_valid = False

elif fruit == 'grapes':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = 3.85
    elif day == 'Saturday' or day == 'Sunday':
            price=4.20
    else:
        is_valid = False
else:
    is_valid = False


sum = (price * quantity)
if is_valid:
  print(f"{sum:.2f}")
else:
    print('error')



