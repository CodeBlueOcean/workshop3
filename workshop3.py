
from itertools import pairwise


hobbies = []

# Review: Lists
# ["Charlie","Alpha","Delta","Bravo"]
# []
# [35,57,57,211,57,232]
# ["nucamp",0,12.5,'Echo']
# All Valid 

# Review: List index
["Charlie","Alpha","Delta","Bravo"]
# What is the index of "Delta"? 2

# Review Bracket notation
my_list = ["Charlie","Alpha","Delta","Bravo"]
print(my_list[0])

# Review Bracket notation
my_list = ["Charlie","Alpha","Delta","Bravo"]
my_list[0] = "Echo"
print(my_list)

# Review: Using Lists
my_list = ["Charlie","Alpha","Delta","Bravo"]
# 1 len(my_list) Length is 4 (number of items)
# my_list.append("Echo") "Echo" added to end of list
# x = my_list.pop() 
# x = my_list.pop(2)

# Review: Slicing notation
my_list = ["Charlie","Alpha","Delta","Bravo"]
# What part of the list is "sliced" by...
# my_list[:3] "Charlie","Alpha","Delta"
# my_list[2:] "Delta","Bravo"
# my_list[1:3] "Alpha","Delta"

# Review: The in Keyword
my_list = ["Charlie","Alpha","Delta","Bravo"]
# 1) print("Alpha" in my_list)     "True"
# 2) if "Delta" not in list:      "Delta"
#         print("No Delta")
#    else: 
#         print("Delta")
# 3) print("Echo" in my_list)       "False"

# Review: For loops
my_list = ["Charlie","Alpha","Delta","Bravo"]

for word in my_list:
    print(word)

for idx in range(0, len(my_list), 1):
    print(my_list[idx])

# Review: Strings
lang = "Python"
print(lang[0])

lang[0] = "M"

# Review: Strings 
for char in "Bravo":
    print(char)

# Tuples, set, list, dicitionary are interable

# Review: Dictionaries

brain = {
    'name': 'Brain' 
}

brain = {
    'Brain' 
}
# python sees it as a set, not dictionaries 

brain = {
    'fav-color': 'sea blue', 
    'name': 'Brain Larson'
}

print(brain['name'])


# Review: Dictionaries

ingredients = {"butter": "1 stick", "flour": "2 cups", "salt": "1 tsp"}
ingredients["butter"]
ingredients["flour"] = "2.5 cups"

# Review: Iterating Dictionaries
popcorn_prices = {"small":1.5,"medium":3.5,"large":4}

for size in popcorn_prices.keys():
    print(size)
for price in popcorn_prices.values():
    print(price)
for size, price in popcorn_prices.items():
    print(size, price)

# Review: Tuples
tuple1 = (1,10,100,1000)

tuple1[0]=2 # No
tuple1 = (2,20,200,2000) # Yes

# Review: Tuples
tuple1 = ("Charlie","Alpha","Delta","Bravo")
tuple2 = "Alpha","Echo","Bravo"
tuple3 = ("Delta")                 # Invalid
tuple4 = ()

def do_some_math(a,b): 
    r1 = a+b    
    r2 = a-b

    return r1, r2

('Delta')

# Review: Sets
# my_set = {}
# my_set = set{}

my_set= {4,23,67,1}
for x in my_set:
    print(x)

my_set.add(55)

my_set.discard(23)





