def calculate_average_marks(students):
    average_marks = {}
    top_performer = None
    highest_average = 0

    for name, marks in students.items():
        avg = round(sum(marks) / len(marks), 2)
        average_marks[name] = avg

        if avg > highest_average:
            highest_average = avg
            top_performer = name

    return average_marks, top_performer

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80],
}

average_marks, top_performer = calculate_average_marks(students)

print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
