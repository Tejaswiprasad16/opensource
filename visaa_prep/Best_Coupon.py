x = int(input().strip())
discount1 = 0.1 * x
discount2 = 100
maximum_discount = max(discount1, discount2)
final_amount = x - maximum_discount
print(int(final_amount))
