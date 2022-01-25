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

def Assignment_selection(arr,n):
    merge_sort(arr,0,len(arr)-1)
    string = str(arr[0][0]) + " " + str(arr[0][1]) +"\n"
    count = 1
    curFinishTime = arr[0][1]
    for c in range(1,n):
        if arr[c][0] >= curFinishTime:
            count += 1
            curFinishTime = arr[c][1]
            string += str(arr[c][0]) + " " + str(arr[c][1]) +"\n"
    string = str(count) + "\n" + string    
    string = string[0:len(string)-1]   
    print(string)
    return string

file = open("task1_input.txt",'r')
N = int(file.readline())
arr2d = []
for i in range(N):
    startEnd = file.readline().split()
    startEnd[0] , startEnd[1] = int(startEnd[0]) , int(startEnd[1])
    arr2d.append(startEnd)
output = Assignment_selection(arr2d,N)

file = open("task1_output.txt",'w')
file.write(output)
file.close()