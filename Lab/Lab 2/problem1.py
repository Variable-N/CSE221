def bubble_sort(array):
    for i in range(len(array)):
        sorted = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]
                sorted = False
        if sorted:   # THIS variable remains TRUE if and only if the array is already sorted. in that case, it breaks the loop. So, for the best case scenario, when an array is already sorted, we get the time complexity theta(n) for best case scenario
            break
    
    return array

file = open("input1.txt",'r')
n = file.readline()
a = file.readline().split()
file.close()

for i in range(int(n)): a[i] = int(a[i])
bubble_sort(a)
output = ""
for i in range(int(n)): output+= str(a[i]) + " "
file = open("output1.txt",'w')
file.write(output)
file.close()
