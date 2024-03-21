import random

# Question 1
# This function returns the lowest value
print("Question 1, returns smallest value")


def min3(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z


print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

# Question 2
# This function makes a box

print("\nQuestion 2,makes a box ")


def box(a, b):
    for row in range(a):
        for column in range(b):
            print("*", end=" ")
        print()


box(7, 5)
print()
box(3, 2)
print()
box(3, 10)

# Question 3
# This function finds the location of a number in the list counting from

print(" \nQuestion 3, involves 10,000 numbers in a list ")

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]


def find(my_list, key):
    for number in range(len(my_list)):
        if my_list[number] == key:
            print("number", key, " is found in position", number)


find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

# Question 4

print(" \nQuestion 4, involves 10,000 numbers in a list ")

my_list = []


def list_function(my_list, a):
    # random numbers in the list
    for lists in range(a):
        my_list.append(random.randrange(1, 7))
    print(my_list)


def count_list(my_list):
    # counts of number 1-6 in list
    amount = 0
    for number in my_list:
        if number == 1:
            amount += 1
    print("amount of 1 in list = ", amount)

    amount = 0
    for number in my_list:
        if number == 2:
            amount += 1
    print("amount of 2 in list = ", amount)

    amount = 0
    for number in my_list:
        if number == 3:
            amount += 1
    print("amount of 3 in list = ", amount)

    amount = 0
    for number in my_list:
        if number == 4:
            amount += 1
    print("amount of 4 in list = ", amount)

    amount = 0
    for number in my_list:
        if number == 5:
            amount += 1
    print("amount of 5 in list = ", amount)

    amount = 0
    for number in my_list:
        if number == 6:
            amount += 1
    print("amount of 6 in list = ", amount)


def average_list(my_list):
    # calulates list average
    list_total = 0
    for amount in my_list:
        list_total += amount
    avg = list_total / len(my_list)
    print("Average of list = ", avg)


list_function(my_list, 10000)
count_list(my_list)
average_list(my_list)
