def bs(target=1):
    arr = [1,1,5,6,7,8,9,10,10,23,23,23,23,45,45,90,90,90,90,90,90,91,92,99,99,99,99,99,99]
    arr.reverse()
    print(arr)
    
    if arr[-1]>=target:
        print(arr)
        return len(arr)
    
    l = 0
    r = len(arr)-1
    while (l<r):
        mid = (l+r)//2
        if(arr[mid]>target):
            l = mid+1
        elif(arr[mid]<target):
            r = mid-1
        else:
            break
        
    while(arr[mid]>=target and mid<len(arr)):
        mid+=1
    print(arr[:mid])
    return mid

print(bs(11))