def Merge_sort(list):
    if len(list) == 1:
        return
    
    middle = len(list) // 2
    left_half = list[:middle]
    right_half = list[middle:]

    Merge_sort(left_half)
    Merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            list[k] = left_half[i]
            i = i + 1
        else:
            list[k] = right_half[j]
            j = j + 1
        
        k = k + 1

    while i < len(left_half):
        list[k] = left_half[i]
        k = k + 1
        i = i + 1

    while j < len(right_half):
        list[k] = right_half[j]
        k = k + 1
        j = j + 1
    return list

if __name__ == "__main__":
    list = [2, 5, 1, 6, 7, 3, 7, 8, 10]
    Merge_sort(list)
    print(list)