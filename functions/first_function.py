def myfunction():
    print("First Function")
myfunction()

def myfunction(a,b):
    sum =a+b
    return sum  #local variable
print(myfunction(2,3))

def myfunction(a):
    table=[]
    for i in range(11):
        table.append(a*i)
    return table    #similarky dict ,tuple,class
print(myfunction(2))
a=5
def fun():
    print(a)
def fun2():
    global a
    a=a+5
    print(a)
fun()        
fun2()
