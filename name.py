name = "Super_Coder_2026"

yuy = name.strip().lower().replace("_", "-")

print("მომხმარებელის სახელი: ", yuy)

print("სახელის სიგრძე: ", len(yuy))

print("იწყემა *super*-ით: ", yuy.startswith("super"))

print("ტირეების რაოდენობა: ", yuy.count("-"))

print("მხოლოდ ასოები და ციფრები: ", yuy.replace("-", "").isalnum())
