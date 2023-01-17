import math
record_in_second = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())
resistance = distance_in_meters // 15
added_time  = resistance * 12.5

swimming_meter= distance_in_meters * time_in_seconds
total_time = swimming_meter + added_time

if record_in_second <= total_time:
    print(f"No, he failed! He was {total_time - record_in_second:.2f} seconds slower.")
if record_in_second > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

