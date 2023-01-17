number_groups = int(input())
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
total_sum = 0

for people in range(number_groups):
    number_people = int(input())
    if number_people <= 5:
        g1 += total_sum + number_people
    elif number_people <= 12:
        g2 += total_sum + number_people
    elif number_people <= 25:
        g3 += total_sum + number_people
    elif number_people <= 40:
        g4 += total_sum + number_people
    elif number_people >= 41:
        g5 += total_sum + number_people

total_climbers = g1 + g2 + g3 + g4 + g5


print(f'{g1 / total_climbers * 100:.2f}%')
print(f'{g2 / total_climbers * 100:.2f}%')
print(f'{g3 / total_climbers * 100:.2f}%')
print(f'{g4 / total_climbers* 100:.2f}%')
print(f'{g5 / total_climbers * 100:.2f}%')
