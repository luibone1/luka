yuy = "python2024"


for i in range(3):
    Pass = input("შეიყვანეთ პაროლი: ")

    AttemsLeft = 2 - i


    if Pass == "":
        print(f"არასწორია, დარჩენილი მცდელობები: {AttemsLeft}")
        continue


    if Pass == yuy:
        print("პაროლი სწორია")
        break
    else:
        print(f"არასწორია, დარჩენილი მცდელობები: {AttemsLeft}")


else:
    print("ანგარიში დაბლოკილია")
