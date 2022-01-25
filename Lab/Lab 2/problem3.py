def sort_insertion(unsort_Array,sort_Array):
    string = ""
    for i in range(len(sort_Array)-1):
        if sort_Array[i] < sort_Array[i+1]:
            j = i+1
            while j != 0 and sort_Array[j] > sort_Array[j-1]:
                sort_Array[j],sort_Array[j-1] = sort_Array[j-1],sort_Array[j]
                unsort_Array[j], unsort_Array[j-1] = unsort_Array[j-1], unsort_Array[j]
                j -= 1
        
    for i in range(len(unsort_Array)) : string += str(unsort_Array[i]) +" "
    return string
    


f = open("input3.txt", "r")
n = int(f.readline())
roll = f.readline().split(' ')
marks = f.readline().split(' ')
f.close()
for i in range(n): 
    roll[i] = int(roll[i])
    marks[i] = int(marks[i])

output = sort_insertion(roll,marks)
f = open("output3.txt", 'w')
f.write(output)
f.close()

