def Selection_sort(l):
    
    for i in range(len(l)-1):
        index = i

        for j in range(i+1,len(l)):
            
            if l[j] < l[index]:
                # equivalent of using a swap function   
                l[j],l[index] = l[index],l[j] 

    return l


print(Selection_sort([2,5,1,6,7,3,7,8,10]))
