def selection_sort(array,n,m):
    string = ""
    for i in range(m):
        minIndex = i
        for j in range(i+1, n):
            if array[minIndex] > array[j]:
                minIndex = j
        
        array[i], array[minIndex] = array[minIndex], array[i]
        string += str(array[i]) + " "
    return string

file = open("input2.txt",'r')
n = file.readline().split()
a = file.readline().split()
file.close()
for i in range(int(n[0])): a[i] = int(a[i])

output = selection_sort(a,int(n[0]),int(n[1]))

file = open("output2.txt",'w')
file.write(output)
file.close()