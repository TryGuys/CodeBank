def insertion_sort(l):
    
    for i in range(len(l)):
        
        j = i

        while j>0 and l[j-1] > l[j]:
            
            l[j],l[j-1] = l[j-1],l[j]

            j = j-1            
    return l

print(insertion_sort([2,5,1,6,7,3,7,8,10]))