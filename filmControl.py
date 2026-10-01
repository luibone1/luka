yuy = int(input("ასაკი: "))
withP = input("მშობელთან ერტად ხარ? (კი/არა): ")

if yuy < 12:
      print("ჯერ პატარა ხარ")

elif yuy >= 18:
   print("შესვლა დაშვებულია")

else:
     if withP == "კი":
          print("შესვლა დაშვებულია")
     else:
          print("შესვლა აკრძალულია")
