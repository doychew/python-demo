name = input()
points_academy = float(input())
jury = int(input())

for i in range(jury):
    jury_name = input()
    jury_points = float(input())
    current_jury_points = len(jury_name) * jury_points / 2
    points_academy += current_jury_points
    if points_academy > 1250.5:
        break
if points_academy > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {points_academy:.1f}!")
else:
    diff = 1250.5 - points_academy
    print(f"Sorry, {name} you need {diff:.1f} more!")
