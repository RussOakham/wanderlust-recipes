def calculate_avg_rating(rating):
    # Calculate weighted average rating from rating vote count array.
    cumulative = 0
    sum = 0

    for i in range(1,6):
        cumulative += rating[i] * i
        sum += rating[i]

    if sum > 0 and cumulative > 0:
        average = round(cumulative / sum)
        return average
