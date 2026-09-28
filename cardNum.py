card = "41111222233334444"
phone = "599123456"


mask = '**** **** ****'

firstC = card[:4]

lastC = card[-4:]

cardLen = len(card)

revCard = card[::-1]

Fphone = f'{phone[:3]} {phone[3:5]} {phone[5:7]} {phone[7:]}'


print("შენიღბული: ", mask, lastC)

print("პირველი 4 ციფრი: ", firstC)

print("ციფრების რაოდენობა: ", cardLen)

print("შებრუნებული: ", revCard)

print("ტელეფონი: ", Fphone)
