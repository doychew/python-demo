numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(numbers):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num < 400:
        p2 += 1
    elif current_num < 600:
        p3 += 1
    elif current_num < 800:
        p4 += 1
    else:
        p5 += 1

print(f'{p1 / numbers * 100:.2f}% ')
print(f'{p2 / numbers * 100:.2f}% ')
print(f'{p3 / numbers * 100:.2f}% ')
print(f'{p4 / numbers * 100:.2f}% ')
print(f'{p5 / numbers * 100:.2f}% ')
