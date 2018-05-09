def Quick_sort(list,low,high):
    
    if low >= high:
        return
    pivot = partition(list,low,high)
    Quick_sort(list,low,pivot-1)
    Quick_sort(list,pivot+1,high)
    return list


def partition(list,low,high):
    
    pivot = (low + high) // 2
    swap(list,pivot,high)

    i = low
    for j in range(low,high,1):
        if list[j] <= list[high]:
            swap(list,i,j)
            i = i+1
    swap(list,i,high)

    return i

def swap(list,i,j):
    list[i],list[j] = list[j],list[i]

list = [2, 5, 1, 6, 7, 3, 7, 8, 10]
print(Quick_sort(list,0,len(list)-1))