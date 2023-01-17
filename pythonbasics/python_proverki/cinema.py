type_of_movie = input()
rows = int(input())
columns = int(input())
ticket_price = 0
places = rows * columns

if type_of_movie == "Premiere":
    ticket_price = 12
elif type_of_movie == 'Normal':
    ticket_price = 7.50
elif type_of_movie == 'Discount':
    ticket_price = 5

income = places * ticket_price
print(f'{income:.2f} leva')



