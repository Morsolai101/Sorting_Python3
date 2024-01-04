def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Масив до сортування:", arr)
    print("Масив після сортування:", insertion_sort(arr))