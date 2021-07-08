# A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[-1])
print(thistuple.count("a"))
print(thistuple.index("orange"))

y = list(thistuple)
y.append(("orange",))
thistuple = tuple(y)
print(thistuple)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)