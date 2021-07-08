name=input("Enter Student Name: ")
roll=input("Enter Student roll: ")
std=input("Enter Student std: ")
div=input("Enter Student div: ")
student={
    "name":name,
    "roll":roll,
    "std":std,
    "div":div

}
print(student)
print("Roll no. {} {} is studying in {} {}".format(student["roll"],student["name"],student["std"],student["div"]))