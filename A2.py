def fractional_knapsack(value, weight, capacity):
    ratios = []
    total_value = 0.0 

    for i in range(len(value)):
        ratios.append((value[i] / weight[i], value[i], weight[i]))

    ratios.sort(reverse=True)

    for i in range(len(value)):
        if capacity >= weight[i]:
            total_value += value[i]
            capacity -= weight[i]
        else:
            total_value += (capacity * value[i] / weight[i])
            capacity = 0

    return total_value

values = [60, 100, 120]
weights = [1, 2, 3]
knapsack_capacity = 5

max_value = fractional_knapsack(values, weights, knapsack_capacity)

print("Maximum value:", max_value)
