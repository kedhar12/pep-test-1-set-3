def minimumTrips(weight):
    weight.sort()

    left = 0
    right = len(weight) - 1
    trips = 0

    while left <= right:
        if left < right and weight[left] + weight[right] <= 3.0:
            left += 1
        right -= 1
        trips += 1

    return trips