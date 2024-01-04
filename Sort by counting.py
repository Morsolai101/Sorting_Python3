def counting_sort(arr):
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1
    count_array = [0 for _ in range(range_of_elements)]
    output_array = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        count_array[arr[i] - min_element] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i] - min_element] - 1] = arr[i]
        count_array[arr[i] - min_element] -= 1

    for i in range(len(arr)):
        arr[i] = output_array[i]

if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    counting_sort(arr)
    print("Sorted array:", arr)