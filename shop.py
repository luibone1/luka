try:
    yuy = float(input("ყიდვის თანხა (ლარი):  "))

except ValueError:
    print("გთხოვთ რიცხვი.")
    yuy = 0

if yuy >= 200:
    disP = 20

elif yuy >= 100:
    disP = 10

elif yuy >= 50:
    disP = 5

else:
    disP = 0

disA = yuy * (disP / 100)

fPrice = yuy - disA


vip = input("ვიპ პრომოკოდი (თუ არ გაქვთ - Enter):  ").strip()

if vip.lower() == "vip":
    fPrice -= 5
    print("VIP კოდი: დამატებით -5 ლარი")

print(f"პასდაკლება: {disP}%")
print(f"გადასახადი: {fPrice} ლარი")
