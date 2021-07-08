# A set is a collection which is both unordered and unindexed.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
print(len(thisset))
thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
thisset.remove("banana")

print(thisset)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print(set1.isdisjoint(set2))

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
y={"google"}
print(y.issubset(x))