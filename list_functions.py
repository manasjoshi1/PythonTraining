my_list=["lets","learn","python","in","a","fun","way","  spaces  ","1st"]
my_list.sort()
print(my_list)
my_list.append("nicely sorted")
my_list2=my_list.copy()
print("My_List2: ",my_list2)
my_list2.pop(2)
print(my_list2)
my_list2.remove("fun")
print(my_list2)
my_list2.insert(3,"fun")
print(my_list2)
my_list2.clear()
