#SPA Sorting
# Name:Ankit Kumar Mishra
# Roll No: 2501730079

import random
import time
import sys

sys.setrecursionlimit(20000)


# Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp

    return arr


# Merge Sort

def merge(a, b):
    result = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            result.append(a[i])
            i = i + 1
        else:
            result.append(b[j])
            j = j + 1

    while i < len(a):
        result.append(a[i])
        i = i + 1

    while j < len(b):
        result.append(b[j])
        j = j + 1

    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Quick Sort (Lomuto Partition)

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


# Timing Function

def measure_time(sort_func, arr):

    temp = arr.copy()

    start = time.time()

    if sort_func == quick_sort:
        sort_func(temp, 0, len(temp) - 1)
    else:
        sort_func(temp)

    end = time.time()

    return (end - start) * 1000


# Dataset Generator

def generate_data(n):

    random_list = []

    for i in range(n):
        random_list.append(random.randint(1, 100000))

    sorted_list = random_list.copy()
    sorted_list.sort()

    reverse_list = sorted_list.copy()
    reverse_list.reverse()

    return random_list, sorted_list, reverse_list


# MAIN PROGRAM

if __name__ == "__main__":

    # Correctness Checking
    print("Checking correctness on small list")

    test = [5, 2, 9, 1, 5, 6]
    expected = [1, 2, 5, 5, 6, 9]

    print("Original:", test)

    insertion_result = insertion_sort(test.copy())
    print("Insertion:", insertion_result)

    merge_result = merge_sort(test.copy())
    print("Merge:",  merge_result)

    temp = test.copy()
    quick_sort(temp, 0, len(temp) - 1)
    print("Quick:", temp)

    if insertion_result == expected and merge_result == expected and temp == expected:
        print("All algorithms are correct")
    else:
        print("Error in sorting")


    # Timing Experiments

    print("\nTiming Results (in ms)")

    sizes = [1000, 5000, 10000]

    for n in sizes:

        print("\nSize:", n)

        rand, sorted_arr, rev = generate_data(n)

        print("\nRandom Data")
        print("Insertion:", measure_time(insertion_sort, rand))
        print("Merge:", measure_time(merge_sort, rand))
        print("Quick:", measure_time(quick_sort, rand))

        print("\nSorted Data")
        print("Insertion:", measure_time(insertion_sort, sorted_arr))
        print("Merge:", measure_time(merge_sort, sorted_arr))
        print("Quick:", measure_time(quick_sort, sorted_arr))

        print("\nReverse Data")
        print("Insertion:", measure_time(insertion_sort, rev))
        print("Merge:", measure_time(merge_sort, rev))
        print("Quick:", measure_time(quick_sort, rev))