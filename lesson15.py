import os


def save_scores(path: str, scores: dict[str, int]) -> None:

    with open(path, "w", encoding="utf-8") as file:

        for name, score in scores.items():

            file.write(f"{name}:{score}\n")



def add_score(path: str, name: str, score: int) -> None:

    with open(path, "a", encoding="utf-8") as file:

        file.write(f"{name}:{score}\n")



def read_scores(path: str) -> dict[str, int]:

    scores_dict = {}

    try:
        with open(path, "r", encoding="utf-8") as file:

            for line in file:

                cleaned_line = line.strip()

                if not cleaned_line:

                    continue

                name, score = cleaned_line.split(":")

                scores_dict[name] = int(score)

    except FileNotFoundError:

        print("⚠ ფაილი ვერ მოიძებნა")

        return {}


    return scores_dict



os.makedirs("data", exist_ok=True)

save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})

add_score("data/scores.txt", "დათო", 64)

add_score("data/scores.txt", "მარიამი", 97)


with open("data/scores.txt", encoding="utf-8") as file:

    print(file.read(), end="")


scores = read_scores("data/scores.txt")

print(scores)


total_students = len(scores)

print(f"სტუდენტები: {total_students}")


avg_score = sum(scores.values()) / total_students if total_students > 0 else 0

print(f"საშუალო ქულა: {round(avg_score, 1)}")


best_student = max(scores, key=scores.get)

print(f"საუკეთესო: {best_student} {scores[best_student]}")


passed_path = "data/passed.txt"

with open(passed_path, "w", encoding="utf-8") as file:

    for name, score in scores.items():

        if score >= 80:

            file.write(f"{name}\n")


passed_list = []

with open(passed_path, "r", encoding="utf-8") as file:

    for line in file:

        cleaned_name = line.strip()

        if cleaned_name:

            passed_list.append(cleaned_name)
            

print(f"ჩააბარეს (80+): {passed_list}")
