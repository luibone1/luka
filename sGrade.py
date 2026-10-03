def main():

    try:
        nameIn = input("შეიყვანეთ სახელი:  ")

        name = nameIn.strip()

        if not name:
            raise ValueError("სახელი ვერ იქნება ცარიელი")

        try:
            scoreIn = input("მიღებული ქულა:  ")

            score = int(scoreIn)

            maxScoreIn = input("მაქსიმალური ქულა:  ")

            maxScore = int(maxScoreIn)

        except ValueError:
            raise TypeError("ქულა ნატურალური რიცხვებით ჩაწერეთ")

        if maxScore == 0:
            raise ZeroDivisionError("მაქსიმალური ქულა 0 ვერ იქნება")

        if score < 0 or maxScore < 0 or score > maxScore:
            raise IndexError("ქულა არასწორ დიაპაზონშია")

    except ValueError as A:
        print(f"X {A}")

    except TypeError as A:
        print(f"X {A}")

    except ZeroDivisionError as A:
        print(f"X {A}")

    except IndexError as A:
        print(f"X {A}")

    else:
        yuy = (score / maxScore) * 100

        yuy2 = name[0]

        if yuy >= 100:
            yuy1 = "A"
        elif score >= 90:
            yuy1 = "B"
        elif score >= 80:
            yuy1 = "C"
        elif score >= 70:
            yuy1 = "D"
        elif score >= 60:
            yuy1 = "E"
        elif score >= 50:
            yuy1 = "FX"
        else:
            yuy1 = "LOOSER"

        print(f"{yuy2}. {name} - {yuy:.1f}% - შეფასება: {yuy1}")

    finally:
        print("შეფასების სისტემამ მუშაობა დაასრულა")

if __name__ == "__main__":
    main()
