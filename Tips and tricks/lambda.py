#anyonymous functions / lambda expressions
#%%
#usually
def f(x):
    return 3 * x + 1

f(2)
# %%
#format
#lambda input: return_expression
lambda x: 3*x+1

#but how do we use it?

#%%
#give it a name
g = lambda x: 3*x+1
g(2)

#%%
#you can also use paranthesis to pass in the arguments after the expression
(lambda x: 3*x+1)(2)

# %%
#more than one input?
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
full_name("    fIrstofF", "MYNAME")

# %%
#example with no name
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett", "Robert Jordan"]

#let's say we wanna sort it by last name
help(scifi_authors.sort) # we can use the key argument as a function for sorting
# %%
#let's pass in a lambda expression to do so
scifi_authors.sort(key = lambda name: name.split(" ")[-1].lower())
scifi_authors

# %%
#function of functions
# quadratic formula: f(x) = ax^2 + bx + c
def build_quadratic_func(a,b,c): #inputs are coefficients
    """ Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_func(2,3,-5)
f(0)
# %%
f(1)
# %%
f(2)
# %%
build_quadratic_func(3,0,1)(2) #3x^2 + 1


# %%
#used commonly in combination with Python's map function - map(fun, iter)

def my_map(my_func, my_iter):
    "simplified version of map function - for illustration purposes"
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return result

cubed = my_map(lambda x: x**3, numbers)

#%%
#instead of this:
def doubler(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(doubler, numbers)
print(list(result))

# %%
#use lambda + map
numbers = {1, 2, 3, 4}      # works with lists, tuples or sets
result = map(lambda x: x + x, numbers)
print(list(result))
# %%
