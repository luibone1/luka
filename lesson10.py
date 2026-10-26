
EXTRA_PRICES = {"popcorn": 6, "cola": 3, "nachos": 7}


def book_tickets(movie, *seats, discount=0, **extras):


    is_valid = lambda seat: (

        len(seat) >= 2 and

        seat[0] in "ABCDE" and

        seat[1:].isdigit() and

        1 <= int(seat[1:]) <= 10
    )


    valid_seats = list(filter(is_valid, seats))

    rejected_count = len(seats) - len(valid_seats)



    seat_price = lambda seat: 15 if seat[0] in "AB" else 10

    ticket_prices = list(map(seat_price, valid_seats))



    tickets_total = sum(ticket_prices) * (1 - discount / 100)



    extras_total = sum(extras.get(item, 0) * quantity for item, quantity in extras.items())


    total_price = round(tickets_total + extras_total, 2)


    return {
        "movie": movie,

        "seats": valid_seats,

        "rejected": rejected_count,

        "total": total_price
    }



order1 = book_tickets("ოპენჰაიმერი", "A5", "C3", "Z1", "B12", "E10")

order2 = book_tickets("დიუნა", "B1", "B2", discount=20, popcorn=2, cola=2)

order3 = book_tickets("ინტერსტელარი", "D4", nachos=1)

order4 = book_tickets("ბარბი")

for order in [order1, order2, order3, order4]:
    print(f"{order['movie']}: ადგილები {order['seats']}, უარყოფილი: {order['rejected']}, სულ: {order['total']} ლარი")
