def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3,454,5]
    n = len(arr)
    shellSort(arr)
    print("Sorted array: ")
    for i in range(n):
        print(arr[i], end=" ")
