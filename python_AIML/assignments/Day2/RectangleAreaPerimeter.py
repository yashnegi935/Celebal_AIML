length = float(input("Enter length in cm: "))
breadth = float(input("Enter breadth in cm: "))

perimeter = 2 * (length + breadth)
area = length * breadth

perimeter_inches = perimeter / 2.54
area_inches = area / (2.54 * 2.54)

print(f"Perimeter in inches: {perimeter_inches:.2f}")
print(f"Area in square inches: {area_inches:.2f}")