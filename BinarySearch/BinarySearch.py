def binary_search(arr: list, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == val:
            return mid
        elif guess > val:
            high = mid - 1
        else:
            low = mid + 1
    return

