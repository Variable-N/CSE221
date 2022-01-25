def activities (tasks, call):
    jackT = []
    jillT = []
    seq = ""
    jackH = 0
    jillH = 0
    for i in call:
        if i == "J":
            jackT.append(min(tasks))
            seq += str(min(tasks))
            jackH += min(tasks)
            tasks.remove(min(tasks))
        else:
            jillT.append(max(jackT))
            seq += str(max(jackT))
            jillH += max(jackT)
            jackT.remove(max(jackT))

    seq += "\nJack will work for {} hours\nJill will work for {} hours".format(jackH,jillH)
    print(seq)
    return seq
    

file = open("task3_input.txt",'r')
N = int(file.readline())
hours = file.readline().split()
for i in range(len(hours)): hours[i] = int(hours[i])
call = file.readline()

output = activities(hours,call)
file = open("task3_output.txt",'w')
file.write(output)
file.close()