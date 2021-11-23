import numpy as np

# 1
x = 0
x = x == x
print(x)
# out: True

# 2
list1 = [1, 2, 3]
list2 = list1[-2:-1]
list3 = list2[-1:-2]
print(list2, list3)
# out: [2] []

# 3
oldList = [1, 2, 3]
for i in range(len(oldList)):
    oldList.insert(i, 0)
print(oldList)
# out: [0, 0, 0, 1, 2, 3]

# 4
my_list = [1, 2, 3, 4, 5]
my_list[1], my_list[2] = my_list[2], my_list[1]
print(my_list)
# out: [1, 3, 2, 4, 5]

# 5
alphabets = ['a', 'b', 'c']
del alphabets[:]
print(alphabets)
# out: []

# 6
lst = [4, 5, 7] * 3 + [8]
print(len(lst))
# out: 10

# 7
# my_color = 'Yellow'
# my_color[5] = 's'
# print(my_color)
# out: TypeError: 'str' object does not support item assignment

# 8
my_values = (1, 2, 3, 4)
my_values = my_values[1:-1]
my_values = my_values[1]
print(my_values)
# out: 3

# 9
print(type(range(20)))

# 10
print('+100 200+ 300+')

# 11
print(print())

# 12
print('\t\x23')

# 13
a = 50
b = a
print(id(a))
print(id(b))
# One Object, Two Reference

# 14
t = (1, 'Data', 2 + 5j)
print(t[2:3])
# print(np.dtype(t[2]))
print(type(t[2:3]))
res = t[1:1]
print(type(res))

# 15
print(type(int))
print(type(type(int)))

# 16
print(int())  # will print the default values
print(float())
print()

# 17
try:
    print(X)
except:
    print("An exception occurred.")

# 18
try:
    f = open("test-file.txt")
    f.write("Hello, World!")
except:
    print(
        "Something went wrong.")  # this will print because as we used 'write' method but didn't mention the read or write mode while opening the file


# finally:
# f.close()

# 19
def func():
    print(v + 1, end='')


v = 2
func()
print(v)


a = 5
b = 5
print(a is b)


