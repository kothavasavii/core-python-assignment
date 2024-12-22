def book_seat(booked_seats,seat):
    if seat in booked_seats:
        return "sorry,the seat is already booked"
    else:
        booked_seats.append(seat)

def cancel_seat(booked_seats,seat):
    booked_seats.remove(seat)

def get_available_seats(total_seats,booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

total_seats = 10
print("total_seats = 10")

booked_seats = [2, 5, 7]
print("booked_seats = ",booked_seats)

book=int(input("book_seat ="))
book_seat(booked_seats,book)

cancel=int(input("cancel_seat ="))
cancel_seat(booked_seats,cancel)

print("Available seats:",get_available_seats(total_seats,booked_seats))