def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

def calculate_total_fare(trips):
    total_fare = 0
    for i, distance in enumerate(trips, start=1):
        fare = calculate_fare(distance)
        print(f"Trip {i}: {fare}")
        total_fare += fare
    print(f"Total Fare: ${total_fare}")

tips = [5, 10, 3]
calculate_total_fare(tips)
