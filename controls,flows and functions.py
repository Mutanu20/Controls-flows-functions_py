def calculate_discount( price,discount_percent)
if discount_percent>=20
discount_amount= price *(discount_percent/100)
final price= price-discount_amount
return final_price
else:
    return price

original_price=float(input("Enter the original price:"))
disount_percent=float(input("Enter the discount percentage:"))

final_price=calculated_discount(original_price,discount_percent)

if final price!=original_price:
    print(f"Final price after discount:${final_price:.2f}")
else:
    print(f"No discount applied.Original Price:${original_price:.2f}")
