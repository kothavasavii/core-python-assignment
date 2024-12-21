def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return 0.0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    total_count = len(ratings)
    return round((positive_count / total_count) * 100, 2)

ratings = [5, 4, 3, 5, 2, 4, 1, 5]

positive_percentage = calculate_positive_feedback_percentage(ratings)
print(f"Positive Feedback: {positive_percentage}%")
