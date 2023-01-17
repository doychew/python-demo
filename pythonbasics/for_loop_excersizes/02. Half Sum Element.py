import sys

numbers = int(input())
total_sum = 0
max_num = -sys.maxsize
for number in range(numbers):
    current_num = int(input())
    total_sum += current_num
    if current_num > max_num:
        max_num = current_num
        total_sum += current_num

if max_num == total_sum - max_num:
    print('Yes')
    print(f"Sum =  {total_sum} ")
else:
    print('No')
    total_sum = total_sum - max_num
    print(f"Diff =  {abs(max_num - total_sum)}")