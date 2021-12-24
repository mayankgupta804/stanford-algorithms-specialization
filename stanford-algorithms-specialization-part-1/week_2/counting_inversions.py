def count_inversions(a, start, end):
    if len(a) == 1:
        return 0
    x, y, z = 0, 0, 0
    if start < end:
        mid = (start + end) // 2
        x = count_inversions(a, start, mid)
        y = count_inversions(a, mid + 1, end)
        z = count_split_inversions(a, start, mid, end)
    return x + y + z


def count_split_inversions(a, start, mid, end):
    temp = [0] * (end - start + 1)
    i, j, k, inv_count = start, mid + 1, 0, 0

    while i <= mid and j <= end:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i = i + 1
        else:
            temp[k] = a[j]
            j = j + 1
            inv_count = inv_count + len(a[i:mid + 1])

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

    return inv_count


if __name__ == "__main__":
    with open("numbers.txt") as f:
        data = f.readlines()
        transformed_data = list(map(lambda d: int(d), data))
        print("No. of inversions: ", count_inversions(transformed_data, 0, len(transformed_data) - 1))
