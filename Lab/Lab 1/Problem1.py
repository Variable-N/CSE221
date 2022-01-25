

def isParity (number):
    if isinstance(number,float): return "{} cannot have parity".format(number)
    if number%2 == 0: return "{} has even parity".format(number)
    else: return "{} has odd parity".format(number)

def isPalindrome (word=""):
    if word == "": return "Given word is not a palindrome\n"
    N = len(word)
    for i in range(N//2):
        if word[i] != word[N-1-i]: return "{} is not a palindrome\n".format(word)
    return "{} is a palindrome\n".format(word)

f= open("input.txt")
inputs = f.read().split('\n')

odd = 0  
even = 0
palindrome = 0
total = 0
finalText = ""
for lines in inputs:
    total += 1
    num = lines.split()
    if '.' in num[0]: num[0] = float(num[0])
    else: num[0] = int(num[0])
    string1 = isParity(num[0]) + " and " + isPalindrome(num[1])
    if "odd" in string1 : odd+=1
    elif "even" in string1 : even+=1
    if "is a palindrome" in string1: palindrome+=1
    finalText += string1


output = open("output.txt",'w')
output.write(finalText)

finalRecord = "Percentage of odd parity: {}%\nPercentage of even parity: {}%\nPercentage of no parity: {}%\nPercentage of palindrome: {}%\nPercentage of non-palindrome: {}%".format(int((odd/total)*100),int((even/total)*100),int(((total-odd-even)/total)*100),int((palindrome/total)*100),int(((total-palindrome)/total)*100))
record = open("record.txt",'w')
record.write(finalRecord)


