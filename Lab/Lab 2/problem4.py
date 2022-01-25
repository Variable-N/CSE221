def merge(A,left,mid,right):
    global count
    n1 = mid - left + 1
    n2 = right - mid
    L = []
    R = []
    for i in range(1,n1+1):
        L.append(A[left+i-1])
    for i in range(1,n2+1):
        R.append(A[mid+i])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(left,right+1):
        count += 1
        if L[i] > R[j]:
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

count = 0
# array = [22,32,42,68,81,92]
# merge_sort(array,0,6)
# print(count)


file = open("input4.txt",'r')
n = file.readline()
a = file.readline().split()
file.close()

for i in range(int(n)): a[i] = int(a[i])
merge_sort(a,0,len(a)-1)
output = ""
for i in range(int(n)): output+= str(a[i]) + " "
file = open("output4.txt",'w')
file.write(output)
file.close()
