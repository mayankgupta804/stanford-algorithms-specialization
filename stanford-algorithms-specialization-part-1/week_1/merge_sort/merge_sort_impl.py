def merge_sort(a, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid + 1, end)
        merge(a, start, mid, end)


def merge(a, start, mid, end):
    temp = [0] * (end - start + 1)
    i, j, k = start, mid + 1, 0

    while i <= mid and j <= end:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i = i + 1
        else:
            temp[k] = a[j]
            j = j + 1
        k = k + 1

    while i <= mid:
        temp[k] = a[i]
        i = i + 1
        k = k + 1

    while j <= end:
        temp[k] = a[j]
        j = j + 1
        k = k + 1

    i = start

    while i <= end:
        a[i] = temp[i - start]
        i = i + 1


if __name__ == "__main__":
    arr = [5, 4, 1]
    print("Before merging: ", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("After merging: ", arr)
