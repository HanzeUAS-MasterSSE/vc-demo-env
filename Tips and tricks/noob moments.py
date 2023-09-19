# Using Manual string formatting
def manual_str_formatting(name, followers):
    if followers > 100000:
        print("Wow " + name + "! you have " + str(followers) + " followers!")
    else:
        print("Lol " + name + " that's not many followers")

    # better
    if followers > 100000:
        print(f"Wow {name}! you have {followers} followers!")
    else:
        print(f"Lol {name} that's not many followers")


# Manually Closing a File
f = open(filename, "w")
f.write("hello!\n")
f.close()

with open(filename, "w") as f:
    f.write("hello!\n")
# close automatic, even if exception



# Not using comprehensions, or maybe only using list comprehensions
squares = {}
for i in range(10):
    squares[i] = i * i

# different comprehensions
dict_comp = {i: i * i for i in range(10)}
list_comp = [x*x for x in range(10)]
set_comp = {n%3 for n in range(10)}
gen_comp = (2*y+5 for y in range(10))



#Checking for Type with ==
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

if type(p) == tuple: #Violates Liskov substitution principle (coz subclass)
    print("it's a tuple")
else:
    print("it's not a tuple")

# probably meant to check if is instance of tuple
if isinstance(p, tuple):
    print("it's a tuple")
else:
    print("it's not a tuple")



# Using == for equality in singletons
if x == None:
    pass

if x == True:
    pass

if x == False:
    pass

# check for identity instead
if x is None:
    pass

if x is True:
    pass

if x is False:
    pass



# Using if bool, or if len isn't zero
if bool(x):
    pass

if len(x) != 0:
    pass

# usually equivalent to
if x:
    pass



# Using null-coalescing assignments
x = 10

if x:
    y = x  
else:
    y = "foobar"

# instead use
y = x or "foobar"

print (y)

#also useful for default inputs
x = input()

y = [x or 10]



# Looping over indexes instead of items directly
a = [1, 2, 3]
for i in range(len(a)):
    v = a[i]
    ...

# instead, just loop over items directly
for v in a:
    ...

# or if you wanted the index, use enumerate
for i, v in enumerate(a):   # for lists
    ...

a_dict = {'first': 1}
for i, v in a_dict.items():   # for dictionaries
    ...


# Using index to sync between two lists
a = [1, 2, 3]
b = [4, 5, 6]
for i in range(len(b)):
    av = a[i]
    bv = b[i]
    ...

# use zip instead
for av, bv in zip(a, b):
    ...

#and if you still need the index, couple it with enumerate
for i, (av, bv) in enumerate(zip(a, b)):
    ...



# Similarly, instead of using counter variables when iterating
l = [1, 2, 3]

i = 10
for x in l:
    ...
    i += 1

#just use enumerate
for i, x in enumerate(l, start=10):
    ...



# Looping over the keys of a dict
d = {"a": 1, "b": 2, "c": 3}
for key in d.keys():
    ...

# that's the default anyway
for key in d:
    ...

# or if you meant to make a copy of keys (coz you're modifying the dict)
for key in list(d.keys()):
    ...

# this should still work
for key in list(d):
    ...



# Using keys to loop over items in dict
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    val = d[key]
    ...

for key, val in d.items():
    ...



# Not using tuple unpacking 
# (if you have a tuple and want to get all it's elements out as variables)
mytuple = 1, 2
x = mytuple[0]
y = mytuple[1]

x, y = mytuple

# or using temporary variables to swap variables
x = 0
y = 1

tmp = x
x = y
y = tmp

# instead of just using tuples
x, y = 0, 1
x, y = y, x


#%%
# Using time.time to time code
import time
start = time.time()
time.sleep(10)
end = time.time()
print(end - start)

#%%
# use (the more accurate) perf_counter
import time
start = time.perf_counter()
time.sleep(10)
end = time.perf_counter()
print(end - start)


#%%
# Doing Math/Data Analysis in Basic Python 
x = list(range(100))
y = list(range(100))
s = [a + b for a, b in zip(x, y)]

# use numpy/pandas or other libraries that are built for that
# this is better (faster)
x = np.arange(100)
y = np.arange(100)
s = x + y



# Not following PEP8
x = (1, 2)
y=5
l = [1,2,3]

def func(x =  5):
    ...

# doesn't make a difference in execution
x = 1, 2
y = 5
l = [1, 2, 3]
j = y**2

def func(x=5):
    ...
# but will make other devs less pissed at you

# Happy Coding :)

# %%
