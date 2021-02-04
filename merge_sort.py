def main():
    arr = [1, 4, 7, 2, 5, 8, 3, 3, 9, 10, 9, 9, 6]
    mergeSort(arr)
    print(arr)


def mergeSort(arr: list):
    if len(arr) < 2 or arr is None:
        return
    process(arr, 0, len(arr) - 1)


def process(arr, left, right):
    if left == right:
        return
    mid = left + ((right - left) >> 1)
    process(arr, left, mid)
    process(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    p1 = left
    p2 = mid + 1
    help = []
    while p1 <= mid and p2 <= right:
        if arr[p1] <= arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1

    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1

    while p2 <= right:
        help.append(arr[p2])
        p2 += 1

    for i in range(len(help)):
        arr[left + i] = help[i]


if __name__ == '__main__':
    main()
