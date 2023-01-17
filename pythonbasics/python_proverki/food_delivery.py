chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
price_delivery = 2.50

quantity_chicken_menu = int(input())
quantity_fish_menu = int(input())
quantity_vegan_menu = int(input())

price_for_chicken_menus = quantity_chicken_menu * chicken_menu_price
price_for_fish_menus = quantity_fish_menu * fish_menu_price
price_for_vegan_menu = quantity_vegan_menu * vegan_menu_price
total_price_menus = price_for_chicken_menus + price_for_fish_menus + price_for_vegan_menu
desert_price = total_price_menus * 0.2
total_price = total_price_menus + desert_price + price_delivery
print(total_price)
