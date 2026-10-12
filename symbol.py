yuy = input("შეიყვანეთ სიტყვა : ")
yuy1 = input("შეიყვანეთ სიმბოლო რომლის დათვლა გინდათ (კი, მე არის იცი ქართული): ")

yuy2 = 0


for letter in yuy:
    if letter == yuy1:
        yuy2 += 1


print(f"The character '{yuy1}' appears {yuy2} times.")
