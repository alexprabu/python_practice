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

# 20
a = 5
b = 5
print(a is b)

# 21
val1 = 5
print('Id of val1: ', id(val1))
val1 = val1 + 1
print('Id of val1: ', id(val1))

print('Id of 6: ', id(6))
# Output
# Id of val1:  2244296665520
# Id of val1:  2244296665552
# Id of 6:  2244296665552


# 22
d1 = {"John": 40, "Peter": 45}
d2 = {"John": 466, "Peter": 45}
print(d1 == d2)

d1 = {"John": 466, "Peter": 45}
d2 = {"John": 466, "Peter": 45}
print(d1 == d2)

# print(d1 > d2)  # will throw -> TypeError: '>' not supported between instances of 'dict' and 'dict'

# 23
dictionary = {1: "SIT", 2: "Dept", 3: "IT"}
print("test1: ", "SIT" in dictionary)
print("test2: ", 1 in dictionary)

# 24
print(dictionary)
del dictionary[3]  # deleting element of key 3
print(dictionary)
del dictionary
# print(dictionary) #will throw error

# 25
a = "hello"
b = "hello"
print(a is b)
print(a == b)
print(id(a), id(b))

a = 'hello world'
b = 'hello world'
print(a is b)
print(a == b)
print(id(a), id(b))

a = ["hi", "hello"]
b = ["hi", "hello"]
print(a is b)
print(a == b)
print(id(a), id(b))

# 26
str = ''
print(bool(str))  # will give False, if we give a space or value it will return True

# 27
a = {i: i * i for i in range(6)}
print(a)  # dict

a = {i * i for i in range(6)}
print(a)  # set

a = (i * i for i in range(6))  # will give tuple, generator object, we have to loop it to get
print(a)  # tuple generator
for item in a:
    print(item)

# 28
c = 5
d = 2
print(c // d)

# 29
v = 2
w = 3
x = 4
y = 19
z = 23
a = v ** v // x % x + y % w * z // x
print("a: ", a)

b = v ** (v // x) % x + y % (w * z) // x
print("b: ", b)

print(1 % 4)  # divide panna mudinja, it will return reminder otherwise athey number return pannum

# 30
print('\n\n')

x = "I Love Python!"
y = "I Love Python!"

print(x == y)
print(x is y)
print(id(x) == id(y))

print(id(x))
print(id(y))

# 31
# x1 = y1 = [1, 2]  # try uncomment this to get different results (same id for both x1 and y1, appending in x1 will reflect in y1)

x1 = [1,2]
y1 = [1,2]


print(x is y)
print(id(x1))
print(id(y1))

x1.append(3)
print(x1)
print(y1)

print(id(x1))
print(id(y1))
