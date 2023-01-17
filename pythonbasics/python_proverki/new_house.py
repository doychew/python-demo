type_flowers = input()
num_flowers = int(input())
budget = int(input())
price = 0
discount = 0
if type_flowers == 'Roses':
    price = 5
elif type_flowers == 'Dahlias':
    price = 3.80
elif type_flowers == 'Tulips':
    price = 2.8
elif type_flowers == 'Narcissus':
    price = 3
elif type_flowers == 'Gladiolus':
    price = 2.5

final_sum = num_flowers * price

if type_flowers == 'Roses' and num_flowers > 80:
    final_sum *= 0.9
elif type_flowers == 'Dahlias' and num_flowers > 90:
    final_sum *= 0.85
elif type_flowers == 'Tulips' and num_flowers > 80:
    final_sum *= 0.85
elif type_flowers == 'Narcissus' and num_flowers < 120:
    final_sum += final_sum * 0.15
elif type_flowers == 'Gladiolus' and num_flowers < 80:
    final_sum += final_sum * 0.2
difference = abs(budget - final_sum)

if budget >= final_sum:
    print(f"Hey, you have a great garden with {num_flowers} {type_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")



