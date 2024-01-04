def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)

    bucket_range = max_value - min_value
    bucket = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_value) / (bucket_range / (len(arr) - 1)))
        bucket[index].append(num)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    result = []
    for sublist in bucket:
        for num in sublist:
            result.append(num)

    return result
if __name__ == "__main__":
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    arr_sorted = bucket_sort(arr)
    print("Sorted array:", arr_sorted)