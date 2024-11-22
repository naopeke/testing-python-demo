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