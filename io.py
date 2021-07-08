# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
print('I love {} and {}'.format('bread','butter'))
print('I love {0} and {1}'.format('bread','butter'))

print('I love {1} and {0}'.format('bread','butter'))
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
num =  1 #int(input('Enter a number: '))
print("Int : %2d, Flost : %5.2f" % (num, 05.333))
print("Total students : %3d, Boys : %2d" % (240, 120))
cstr = "Good Morning world"
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
print (cstr.ljust(40, '-'))
print (cstr.rjust(40, '-'))
x, y = input("Enter a two value: ").split()
print("x: ", x)
print("y: ", y)

x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)