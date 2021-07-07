str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string


#Striping the string
str2="      Hello World!     " #string with spaces
print(len(str2))

print(len(str2.strip()))
print(len(str2.rstrip()))
print(len(str2.lstrip()))

#Slicing the string
#slice() constructor takes three params(start, stop,step)
print(str[slice(2)])
print(str[slice(0,3)])
print(str[slice(0,8,2)])

print(str[slice(-2)])
print(str[slice(-1,-12,-2)])
print(str[slice(-5,-1)])

