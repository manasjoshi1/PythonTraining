def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield one or more statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)