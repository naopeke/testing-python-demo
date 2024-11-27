price = 9.99
discount = 0.2
result = price * (1 - discount)
print(result)

name = "Rodolfo"
print(name)
print(name * 2)

# Create two variables, var1 and var2, both with the same value.
var1 = 3
var2 = 3

# Create two variables, num1 and num2, which multiply together to give 16.
num1 = 2
num2 = 8
print(num1 * num2)

# f-string
name = "Bob"
greeting = f"Hello, {name}"
print(greeting)

# Template strings with .format()
name = "Kevin"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")
print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)

# string formatting
name = input("Enter your name: ")
print(name)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres:.2f} square metres.") # .2f 下２桁

user_age = int(input("Enter your age: "))
# years = int(user_age)
months = user_age * 12
print(f"Your age, {user_age}, is equal to {months} months.")

# list
l = ["Miguel", "Tom", "Ana"] # list, can add and remove
t = ("Miguel", "Tom", "Ana") # tuples, cannot add and remove
# my_tuple = (3,) my_tuple = 3, To create a tuple with a single value in Python, you need to include a comma after the value 
s = {"Miguel", "Tom", "Ana"} # set, can add and remove, bus cannot duplicate. Order could change at any moment

print(l[0]) # Miguel  cannot use for set

l[0] = "Lopez"
print(l) #['Lopez', 'Tom', 'Ana']

l.append("Smith")
print(l) #['Lopez', 'Tom', 'Ana', 'Smith']

s.add("Diego")
print(s) # it isn't append

# usage of set DIFFERENCE
friends = {"Miguel", "Tom", "Ana"}
abroad = {"Miguel", "Ana"}

local_friends = friends.difference(abroad)
print(local_friends) #{'Tom'}

# usage of set UNION
local = {"Tom"}
abroad = {"Miguel", "Ana"}

friends = local.union(abroad)
print(friends) #{'Tom', 'Miguel', 'Ana'}

# usage of set INTERSECTION
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both) #{'Jen', 'Bob'}

# booleans
print(5 == 5) #true
print(5 > 5)  #false
print(10 != 10) #false


friends = ["Miguel", "Tom"]
abroad = ["Miguel", "Tom"]

print(friends == abroad) #true
print (friends is abroad) #false the lists themselves are different

friends = ["Miguel", "Tom"]
abroad = friends
print (friends is abroad) #true

# if
day_of_week = input("What day of the week is it today? ").lower() # lower case

if day_of_week == "monday": 
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's Tuesday")
else:
    print("Full speed ahead!")

print("This always runs")