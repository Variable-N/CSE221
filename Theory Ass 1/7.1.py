def less_than_equal (sorted_array,unsorted_array):
    output = []
    for i in unsorted_array:
        high = len(sorted_array)-1
        low = 0
        while(low<=high):
            mid  = (low + high) // 2
            if sorted_array[mid] > i : high = mid-1 
            else: low = mid+1
        if mid > -1 and sorted_array[mid] > i: mid -= 1 
        output.append(mid + 1)
    return output
print(less_than_equal([1,1,2,2,5],[3,1,4,1,5]))