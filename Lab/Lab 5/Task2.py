def merge(A,left,mid,right):
    n1 = mid - left + 1
    n2 = right - mid
    L = []
    R = []
    for i in range(1,n1+1):
        L.append(A[left+i-1])
    for i in range(1,n2+1):
        R.append(A[mid+i])
    L.append([None,float('inf')])
    R.append([None,float('inf')])
    i = 0
    j = 0
    for k in range(left,right+1):
        if L[i][1] < R[j][1]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A,left,right):
    if left < right:
        mid = (left+right)//2
        merge_sort(A,left,mid)
        merge_sort(A,mid+1,right)
        merge(A,left,mid,right)

def Assignment_selection(arr,n,m):
    merge_sort(arr2d,0,len(arr)-1)
    tasks = [-1]*m
    count = 1   
    tasks[0] = arr[0][1]
    for c in range(1,n):
        j = 0
        while j < m:
            if arr[c][0] >= tasks[j]:
                count += 1
                tasks[j] = arr[c][1]
                break
            j += 1
    
    print(count)
    return str(count)


file = open("task2_input.txt",'r')
N = file.readline().split()
M = int(N[1])
N = int(N[0])
arr2d = []
for i in range(N):
    startEnd = file.readline().split()
    startEnd[0] , startEnd[1] = int(startEnd[0]) , int(startEnd[1])
    arr2d.append(startEnd)
output = Assignment_selection(arr2d,N,M)

file = open("task2_output.txt",'w')
file.write(output)
file.close()