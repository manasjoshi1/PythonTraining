# string=input("Enter string")
string ="banana"
vowels=("a","e","i","o","u")
kevin=[]
stuart=[]
string_tmp=""
strLen=len(string)
for i in range(strLen):
    if string[i] not in vowels:
        kevin.append(string[0:strLen-i])
    else:
        stuart.append(string[0:strLen-i])    
print(kevin)  
print(stuart) 