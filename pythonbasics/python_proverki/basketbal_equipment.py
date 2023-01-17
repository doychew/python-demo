year_tax = int(input())

basketball_sneakers_price = year_tax * 0.6
basketball_tracksuit = basketball_sneakers_price * 0.8
basketball_ball =  basketball_tracksuit / 4
basketball_accesories = basketball_ball / 5
total_price_equipment = year_tax + basketball_sneakers_price + basketball_tracksuit + basketball_ball + basketball_accesories
print(total_price_equipment)