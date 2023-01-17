total_number_of_pages = int(input())
pages_hour = int(input())
number_of_days = int(input())

total_hours = total_number_of_pages // pages_hour
hour_per_day = total_hours // number_of_days
print(hour_per_day)