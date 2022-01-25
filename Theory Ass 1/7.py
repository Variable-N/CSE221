def binarySearch(arr , x , low, high):
    while(low<=high):
        mid  = (low + high) // 2
        if (arr[mid] == x):
            low = mid+1

        elif(arr[mid] > x):
            high = mid-1
            
        else:
            low = mid+1
   
    if mid>-1 and arr[mid] > x:
        mid -= 1
        
    return mid + 1

n = input().split()
arr1 = input().split()
arr1 = [int(i) for i in arr1]
arr2 = input().split()
arr2 = [int(i) for i in arr2]

outputArray = [0] * len(arr2)

for i in range(len(arr2)):
    outputArray[i] = binarySearch(arr1, arr2[i], 0, len(arr1) - 1)

print(*outputArray)