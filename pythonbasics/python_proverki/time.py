hour = int(input())
minutes = int(input())
minutes = minutes + 15
hour = hour + minutes // 60
minutes = minutes % 60
if hour >= 24:
    hour = 0
print(f"{hour}:{minutes:02d}")