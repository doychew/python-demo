deposited_sum = float(input())
time_of_deposit = int(input())
year_percentage = float(input())

interest = deposited_sum * year_percentage / 100
month__interest = interest / 12
total_sum = deposited_sum + time_of_deposit  * month__interest
print(total_sum)