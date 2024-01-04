# Функція сортування шелла
def shellSort(arr):
    # Дізнаємося довжину масива
    n = len(arr)
    # Ділимо значиння надви таким чином ділимо масив на дві частини
    gap = n // 2
    # Створюємо while який перевіряє чи gap більше ніж ноль
    while gap > 0:
        # Створюємо for в якому задаємо межі масив від gap до n
        for i in range(gap,n):
            # Створюємо переміну temp точне чине місче числа в масиві
            temp = arr[i]
            # Створюємо переміну j яка запулучає значення i
            j = i
            # Створюємо while який перевіряє чи j не більше або рівне число gap і якщо arr більше temp
            while j >= gap and arr[j-gap] >temp:
                # задаємо значення j, arr[j-gap] 
                arr[j] = arr[j-gap]
                # j = j-gap
                j -= gap
            arr[j] = temp
        gap //= 2
if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3,454,5]
    n = len(arr)
    shellSort(arr)
    print("Відсортований масив: ")
    for i in range(n):
        print(arr[i], end=" ")
