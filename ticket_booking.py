def get_available_seats(total_seats, booked_seats):
    """Return a list of available seats."""
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(booked_seats, seat):
    """Book a seat if it is not already booked."""
    if seat in booked_seats:
        return False, "Seat already booked."
    booked_seats.append(seat)
    return True, "Seat successfully booked."

def cancel_seat(booked_seats, seat):
    """Cancel a booking if the seat is currently booked."""
    if seat not in booked_seats:
        return False, "Seat is not booked."
    booked_seats.remove(seat)
    return True, "Seat booking cancelled."

# Input data
total_seats = 10
booked_seats = [2, 5, 7]

# Booking a seat
book_seat_number = 3
success, message = book_seat(booked_seats, book_seat_number)
print(message)

# Cancelling a seat
cancel_seat_number = 5
success, message = cancel_seat(booked_seats, cancel_seat_number)
print(message)

# Display available seats
available_seats = get_available_seats(total_seats, booked_seats)
print("Available seats:", available_seats)
