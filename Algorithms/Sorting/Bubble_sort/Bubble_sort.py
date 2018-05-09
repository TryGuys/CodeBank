def Bubble_sort(l):
    
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] >l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]   # equivalent of using a swap function

    return l

l = [2,5,1,6,7,3,7,8,10]
print(Bubble_sort(l))