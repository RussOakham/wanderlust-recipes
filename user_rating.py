def calculate_avg_rating(rating):
    # Calculate average rating from rating array.
    sum_num = 0
    for i in rating:
        sum_num = sum_num + i

    avg = round(sum_num / len(rating))
    return avg
