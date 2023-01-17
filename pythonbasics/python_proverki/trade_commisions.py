town = input()
sales = float(input())
is_valid = True
# 0 ≤ s ≤ 500 500 < s ≤ 1 000 1 000 < s ≤ 10 000 s > 10 000
commission = 0
if town == 'Sofia':
    if sales >= 0 and sales <= 500:
        commission = sales * 0.05
    elif sales <= 1000:
        commission = sales * 0.07
    elif sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:
        is_valid = False


elif town == 'Varna':
    is
    if sales >= 0 and sales <= 500:
        commission = sales * 0.45
    elif sales <= 1000:
        commission = sales * 0.075
    elif sales <= 10000:
        commission = sales * 0.1
    elif sales > 10000:
        commission = sales * 0.13
    else:
        is_valid = False

elif town == 'Plovdiv':
    if sales >= 0 and sales <= 500:
        commission = sales * 0.055
    elif sales <= 1000:
        commission = sales * 0.08
    elif sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:
        is_valid =False
else:
    is_valid =False

if is_valid:
    print(f'{commission:.2f}')
else:
    print('error')