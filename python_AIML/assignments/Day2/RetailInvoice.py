buyer = input("Enter buyer name: ")

goods_price = float(input("Enter household goods price: "))
goods_quantity = int(input("Enter household goods quantity: "))

food_price = float(input("Enter processed food price: "))
food_quantity = int(input("Enter processed food quantity: "))

goods_total = goods_price * goods_quantity
goods_gst = goods_total * 5 / 100
goods_amount = goods_total + goods_gst

food_total = food_price * food_quantity
food_gst = food_total * 12 / 100
food_amount = food_total + food_gst

grand_total = goods_amount + food_amount

print("\nRetail Invoice")
print("Buyer:", buyer)
print("-" * 65)
print(f"{'Item':<20}{'Price':>10}{'Qty':>6}{'GST':>10}{'Total':>15}")
print("-" * 65)

print(f"{'Household Goods':<20}{goods_price:>10.2f}{goods_quantity:>6}{goods_gst:>10.2f}{goods_amount:>15.2f}")
print(f"{'Processed Food':<20}{food_price:>10.2f}{food_quantity:>6}{food_gst:>10.2f}{food_amount:>15.2f}")

print("-" * 65)
print(f"Grand Total: ₹{grand_total:.2f}")