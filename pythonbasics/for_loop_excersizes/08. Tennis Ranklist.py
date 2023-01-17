import math

number_tournaments = int(input())
start_points = int(input())
tournaments_won = 0
average_points = 0
final_points = 0
for tournament in range(number_tournaments):
    stage = (input())
    if stage == 'W':
        average_points += 2000
        tournaments_won += 1
    elif stage == 'F':
        average_points += 1200
    elif stage == 'SF':
        average_points += 720
final_points = start_points + average_points
print(f"Final points: {final_points}")
average_points = math.floor(average_points / number_tournaments )
print(f"Average points: {average_points}")
print(f'{tournaments_won / number_tournaments * 100:.2f}%')


