package_pen_price = 5.80
package_marker_price = 7.20
chemichal_price  = 1.20

package_pen = int(input())
package_marker = int(input())
chemichal_liters = int(input())
percentage_discount = int(input()) * 0.01

total_sum_package_pen = package_pen * package_pen_price
total_sum_package_marker = package_marker * package_marker_price
total_sum_chemichal = chemichal_liters * chemichal_price

total_sum_all_materials = total_sum_package_pen + total_sum_package_marker +total_sum_chemichal

price_with_discount = total_sum_all_materials - (total_sum_all_materials * percentage_discount)

print(price_with_discount)
