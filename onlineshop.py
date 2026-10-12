yuy = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}

yuy1 = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}


yuy2 = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("მე", "ლეპტოპი", 1),
    ("მე", "მონიტორი", 5),
]


UserEx = {}
FailUs = set()
TotalRev = 0


print("შედეგი :  ")


for Cus, Prod, Qty in yuy2:

    if Prod not in yuy:
        print(f"სახელი :  'პროდუქტი'  არ იყიდება")
        FailUs.add(Cus)
        continue

    if yuy1[Prod] < Qty:
        print(f"{Cus}: {Prod} - მარაგში  მხოლოდ  {yuy1[Prod]}  ცალია")
        FailUs.add(Cus)
        continue

yuy1[Prod] -= Qty
Cost = yuy[Prod] * Qty
TotalRev += Cost

if Cus not in UserEx:
    UserEx[Cus] = 0
UserEx[Cus] += Cost

print(f"{Cus}: {Prod} x{Qty} = {Cost} ლარი")


print("- ანგარიში -")

for Cus, Total in UserEx.items():
    print(f"{Cus}: {Total} ლარი")

print(f"შემოსავალი :  {TotalRev} ლარი")


yuy3 = [Prod for Prod, Qty in yuy1.items() if Qty == 0]

print (f"ამოწურული :  {yuy3}")


SortFailUs = sorted(list(FailUs))
print(f"წარუმატებელი  შეკვეთა  ჰქონდათ :  {SortFailUs}")
