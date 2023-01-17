budget_film = float(input())
number_of_statist = int(input())
price_for_equipment = float(input())

discount = 0
sum_for_decor = budget_film * 0.1
sum_for_equipment = number_of_statist * price_for_equipment
if number_of_statist >= 150:
    discount = sum_for_equipment * 0.1
sum_for_equipment = sum_for_equipment - discount
total_sum_film = sum_for_decor + sum_for_equipment
last_money = budget_film - total_sum_film
if total_sum_film > budget_film:
    print(f"Not enough money!")
    print(f"Wingard needs {(total_sum_film - budget_film):.2f} leva more.")
if total_sum_film <= budget_film:
    print(f"Action!")
    print(f"Wingard starts filming with {budget_film - total_sum_film:.2f} leva left.")



