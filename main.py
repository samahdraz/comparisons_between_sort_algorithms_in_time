import random
import time


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
        arr[j] = temp


def merge(arr, low, mid, high):
    nLeft = mid - low + 1
    nRight = high - mid
    arrL = []
    arrR = []

    for i in range(0, nLeft):
        arrL.append(arr[low+i])
    for i in range(0, nRight):
        arrR.append(arr[mid+1+i])

    left_index = 0
    right_index = 0
    general_index = low

    while left_index < nLeft and right_index < nRight:
        if arrL[left_index] < arrR[right_index]:
            arr[general_index] = arrL[left_index]
            left_index += 1
            general_index += 1
        else:
            arr[general_index] = arrR[right_index]
            right_index += 1
            general_index += 1

    while left_index < nLeft:
        arr[general_index] = arrL[left_index]
        left_index += 1
        general_index += 1

    while right_index < nRight:
        arr[general_index] = arrR[right_index]
        right_index += 1
        general_index += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    pivot_index = low
    start = low+1
    end = high
    while start <= end:
        if arr[start] <= arr[pivot_index]:
            start += 1
        if arr[end] > arr[pivot_index]:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return end


def quick_sort(arr, low, high):
    if low < high:
        index = partition(arr, low, high)
        quick_sort(arr, low, (index-1))
        quick_sort(arr, (index+1), high)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)


def heap_sort(arr):
    heap_size = len(arr)
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap root(biggest value) with last node
        heap_size -= 1  # cut biggest value from the array
        max_heapify(arr, 0, heap_size)


def max_heapify(arr, i, heap_size):
    largest = i
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)


def generate_random_array(array_size):
    generated_arr = [random.randint(0, 100) for i in range(array_size)]
    return generated_arr


def calculating_time(array):
    for i in range(0, 5):
        if i == 0:
            start_time = time.time()
            selection_sort(array.copy())
            end_time = time.time()
            print("Running time for Selection Sort is :", (end_time - start_time) * 10 ** 3, "ms")
        elif i == 1:
            start_time = time.time()
            insertion_sort(array.copy())
            end_time = time.time()
            print("Running time for Insertion Sort is :", (end_time - start_time) * 10 ** 3, "ms")
        elif i == 2:
            start_time = time.time()
            merge_sort(array.copy(), 0, len(array)-1)
            end_time = time.time()
            print("Running time for Merge Sort is :", (end_time - start_time) * 10 ** 3, "ms")
        elif i == 3:
            start_time = time.time()
            quick_sort(array.copy(), 0, len(array) - 1)
            end_time = time.time()
            print("Running time for Quick Sort is :", (end_time - start_time) * 10 ** 3, "ms")
        else:
            start_time = time.time()
            heap_sort(array.copy())
            end_time = time.time()
            print("Running time for Heap Sort is :", (end_time - start_time) * 10 ** 3, "ms")


size = input("Enter Array Size: ")
unsorted_array = generate_random_array(int(size))
calculating_time(unsorted_array)


