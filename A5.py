# quick sort 
import random
import time

def deterministic_quicksort(arr, comparisons_counter=None):
    if comparisons_counter is None:
        comparisons_counter = [0]  # Counter to keep track of comparisons

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = []
    equal = []
    right = []

    for element in arr:
        comparisons_counter[0] += 1  # Counting the comparison
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    return deterministic_quicksort(left, comparisons_counter) + equal + deterministic_quicksort(right, comparisons_counter)

def randomized_quicksort(arr, comparisons_counter=None):
    if comparisons_counter is None:
        comparisons_counter = [0]  # Counter to keep track of comparisons

    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]  # Randomly choose the pivot
    left = []
    equal = []
    right = []

    for element in arr:
        comparisons_counter[0] += 1  # Counting the comparison
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    return randomized_quicksort(left, comparisons_counter) + equal + randomized_quicksort(right, comparisons_counter)

def main():
    # Generate a random array for testing
    array_size = 1000
    test_array = [random.randint(0, 1000) for _ in range(array_size)]

    # Perform deterministic quicksort and measure the time
    start_time_det = time.time()
    comparisons_counter_det = [0]
    sorted_array_det = deterministic_quicksort(test_array.copy(), comparisons_counter_det)
    end_time_det = time.time()

    # Perform randomized quicksort and measure the time
    start_time_rand = time.time()
    comparisons_counter_rand = [0]
    sorted_array_rand = randomized_quicksort(test_array.copy(), comparisons_counter_rand)
    end_time_rand = time.time()

    # Print the results for deterministic quicksort
    print("Deterministic Quicksort:")
    print("Original Array:", test_array)
    print("Sorted Array:", sorted_array_det)
    print("Number of Comparisons:", comparisons_counter_det[0])
    print("Time taken:", end_time_det - start_time_det, "seconds")
    print()

    # Print the results for randomized quicksort
    print("Randomized Quicksort:")
    print("Original Array:", test_array)
    print("Sorted Array:", sorted_array_rand)
    print("Number of Comparisons:", comparisons_counter_rand[0])
    print("Time taken:", end_time_rand - start_time_rand, "seconds")

if __name__ == "__main__":
    main()
