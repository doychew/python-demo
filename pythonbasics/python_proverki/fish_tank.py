lenght = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = lenght * width * height
volume_in_litters = volume / 1000
volume_filled = percentage * 0.01
needed_litters = volume_in_litters * (1-volume_filled)
print(needed_litters)