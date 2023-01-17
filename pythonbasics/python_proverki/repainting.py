nylon_price = 1.5
paint_per_liter_price = 14.5
paint_thinner_per_litter_price = 5
needed_quantity_nylon = int(input())
needed_quantity_paint_per_liter = int(input())
needed_quantity_paint_thinner_per_litter = int(input())
workers_hours_working = int(input())
total_sum_nylon = (needed_quantity_nylon +  2) * nylon_price
sum_paint = (needed_quantity_paint_per_liter * paint_per_liter_price)
total_sum_paint_per_litter = sum_paint + (sum_paint * 0.1)
total_sum_paint_thinner = needed_quantity_paint_thinner_per_litter * paint_thinner_per_litter_price
bag_price = 0.4
total_sum_materials = total_sum_nylon + total_sum_paint_per_litter + total_sum_paint_thinner + bag_price
total_sum_workers = total_sum_materials * 0.3 *  workers_hours_working
final_price = total_sum_materials + total_sum_workers
print(final_price)
