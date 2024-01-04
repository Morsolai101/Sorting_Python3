def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Знайдемо максимальне та мінімальне значення
    min_value = min(arr)
    max_value = max(arr)

    # Створимо список "комірок"
    bucket_range = max_value - min_value
    bucket = [[] for _ in range(len(arr))]

    # Розмістимо кожен елемент у відповідну "комірку"
    for num in arr:
        index = int((num - min_value) / (bucket_range / (len(arr) - 1)))
        bucket[index].append(num)

    # Сортуємо кожну "комірку" та збираємо результат
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
    print("Відсортований масив:", arr_sorted)