mylist=[1,2,3,4,5]
secondlist=[2,3,4]
cubes=[x**3 for x in mylist]
print(cubes)
evens=[x for x in mylist if(x%2==0)]
print(evens)
prod=1
prod=[prod:=prod*x for x in mylist ]
print(prod[-1])
common=[x for x in mylist if x in secondlist]
print(common)
