n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    current_sum = int(input())

    if i % 2 == 0:
        even_sum += current_sum
    else:
        odd_sum += current_sum

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')

