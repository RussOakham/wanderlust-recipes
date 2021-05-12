""" Calculate weighted average rating from rating vote count array."""


def calculate_avg_rating(rating):
    """ Set variables for us in function """
    cumulative = 0
    sum_total = 0

    for i in range(1, 6):
        cumulative += rating[i] * i
        sum_total += rating[i]

    if sum_total > 0 and cumulative > 0:
        average = round(cumulative / sum_total)
        return average
