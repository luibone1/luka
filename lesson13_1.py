def countdown(start):

    while start >= 1:

        yield start

        start -= 1

    yield "სტარტი! 🚀"



def squares_up_to(limit):

    n = 1

    while n * n <= limit:

        yield n * n

        n += 1



launch = countdown(3)

print(next(launch))

print(next(launch))

print(list(launch))

print(list(launch))


print(list(squares_up_to(50)))

print(sum(squares_up_to(100)))

for square in squares_up_to(20):

    print(square, end=" ")
    
print()
