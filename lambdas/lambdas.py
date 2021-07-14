import functools

cube = lambda x: x *x *x


print(cube(5))
eve_odd = lambda x: "even" if x%2==0 else "odd"

print(eve_odd(5))

x= lambda a,b : a+b
print(x(10,20))

mlist=[1,2,3,4,5,6,7,8,9,10]
new_list=list(filter(lambda x:(x%2==0),mlist))

print(new_list)

new_list = list(map(lambda x: x * 2 , mlist))

print(new_list)
print(functools.reduce(lambda x, y: x+y, mlist))

