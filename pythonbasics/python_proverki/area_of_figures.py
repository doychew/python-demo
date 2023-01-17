import math
figure = input()
side_a = float(input())

if figure == 'square':
    area = (side_a * side_a)
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_b = float(input())
    area = (side_a * side_b)
    print(f"{area:.3f}")
elif figure == "circle":
    area = math.pi *side_a * side_a
    print(f"{area:.3f}")
elif figure == "triangle":
    side_h = float(input())
    area = (side_a*side_h) / 2
    print(f"{area:.3f}")


