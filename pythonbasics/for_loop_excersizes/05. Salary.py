tabs = int(input())
salary = int(input())
fine = 0

for sites in range(1, tabs + 1):
    site_name = input()
    if site_name == "Facebook":
        fine = 150
        salary -= fine
    elif site_name == "Instagram":
        fine = 100
        salary -= fine
    elif site_name == "Reddit":
        fine = 50
        salary -= fine
    if salary <= 0:
        print("You have lost your salary.")
        break
    else:
        fine = 0
if salary > 0:
    print(salary)



