yuy = "Python არის მარტივი, Python არის ძლიერი და Python არის პოპულარული."

yuyCl = yuy.lower().replace(",", "").replace(".", "")


Words = yuyCl.split()

WordC = {}
for word in Words:

    if word in WordC:
        WordC[word] += 1

    else:
        WordC[word] = 1


print("შ ე დ ე გ ი :  ")
for word, count in WordC.items():
    print(f"{word}: {count}")


MostFrW = None

MaxC = -1

for word, count in WordC.items():
    if count > MaxC:
        MaxC = count
        MostFrW = word

print(f"ყ ვ ე ლ ა ზ ე  ხ შ ი რ ი :  '{MostFrW}' ({MaxC} - ჯ ე რ)")

UnWC = len(WordC)

print(f"ს ხ ვ ა  ს ი ტ ყ ვ ა ა :  {UnWC}")
