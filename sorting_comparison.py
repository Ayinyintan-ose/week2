import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_function, data):
    start = time.time()
    sort_function(data.copy())
    end = time.time()
    return end - start

def generate_dataset(size):
    return [random.randint(0, 100000) for _ in range(size)]

print("Sorting Algorithm Performance Analyzer")
while True:
    sorts = ["Bubble Sort", "Merge Sort", "Quick Sort", "Python Built-in Sort", "Compare All", "Quit Sort"]
    for index, sort in enumerate(sorts):
        print(f"{index + 1}. {sort}")
    size = int(input("Enter dataset size (e.g., 1000, 5000, 10000): "))
    dataset = generate_dataset(size)
    print(f"\nDataset of size {size} generated!\n")
    user_input = input("Choose an option: ")

    if user_input == "1":
        time_taken = measure_time(bubble_sort, dataset)
        print(f"Bubble Sort: {time_taken:.5f} seconds")
    elif user_input == "2":
        time_taken = measure_time(merge_sort, dataset)
        print(f"Merge Sort: {time_taken:.5f} seconds")
    elif user_input == "3":
        time_taken = measure_time(quick_sort, dataset)
        print(f"Quick Sort: {time_taken:.5f} seconds")
    elif user_input == "4":
        time_taken = measure_time(sorted, dataset)
        print(f"Python Built-in Sort: {time_taken:.5f} seconds")
    elif user_input == "5":
        for sort_func in [bubble_sort, merge_sort, quick_sort, sorted]:
            time_taken = measure_time(sort_func, dataset)
            print(f"{sort_func.__name__}: {time_taken:.5f} seconds")
    elif user_input == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

