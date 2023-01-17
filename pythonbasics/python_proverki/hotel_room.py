month = input()
nights = int(input())
studio_price = 76
apartment_price = 77

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_price *= 0.7
    elif nights > 7:
        studio_price *= 0.95

elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if nights > 14:
        studio_price *= 0.8

if nights > 14:
    apartment_price *= 0.9


total_sum_apartment = apartment_price * nights
total_sum_studio = studio_price * nights
print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")
