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

# in
friends = ["Miguel", "Tom", "Ana"]
print("Ana" in friends) #true

movies_watched = {"Star Wars", "I am Groot", "Spiderman"}
user_movie = input("Enter something you've watched recently: ")
print (user_movie in movies_watched)

# if with in
movies_watched = {"Star Wars", "I am Groot", "Spiderman"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

number = 7
user_input = input("Enter 'y' if you wwould like to play: ")
if user_input in ("y", "Y"): #whether the input is "y" or "Y"
    user_number = int(input("Guess out number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) in (1, -1):
    # elif number - user_number in (1, -1):
        print("You were off by one.")
    else: 
        print("Sorry, it's wrong")

# loop
number = 7
while True:
    user_input = input("Would you like to play? (y/n) ").lower()
    if user_input == "n":
        break

    user_number = int(input("Guess out number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) in (1, -1):
    # elif number - user_number in (1, -1):
        print("You were off by one.")
    else: 
        print("Sorry, it's wrong")
    

friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")


grades = [35, 67, 98, 200, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)


grades = [35, 67, 98, 200, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)

# list comprenhensions
numbers = [1, 3, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)


numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print(doubled)


friends = ["Rolf", "Sam", "Samantha", "Sauron", "Jen"]
starts_s = []
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)
print(starts_s) #['Sam', 'Samantha', 'Sauron']


friends = ["Rolf", "Sam", "Samantha", "Sauron", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s) #['Sam', 'Samantha', 'Sauron']


friends = ["Sam", "Samantha", "Sauron"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s) #['Sam', 'Samantha', 'Sauron']
print(friends)
print(friends is starts_s) #false friends and starts_s aren't the same
print("friends: ", id(friends), "starts_s: ", id(starts_s)) # using the different memory


friends = ["Sam", "Samantha", "Sauron"]
starts_s = friends
print(friends is starts_s) #true


# dictionaries
friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friends_ages["Adam"]) # 30

friends_ages["Bob"] = 20
print(friends_ages) # {'Rolf':24, 'Adam':30, 'Anne':27, 'Bob':20}

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]
print(friends[0]) #{"Rolf", "age": 24}
print(friends[0]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

#まず、student_attendance 辞書からキー（学生の名前）を1つずつ取り出して、変数 student に格納
#次に、student_attendance[student] でその学生に対応する出席状況を取り出して表示
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

#items() メソッドを使って、student_attendance 辞書からキーと値のペアを同時に取り出し
#各イテレーションで、student には学生の名前が、attendance にはその学生の出席状況が格納
#student と attendance を使って出力
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

# destructuring variables
x = [(5, 11)] #normally not nessesary
x, y = 5, 11

t = 5, 11
x, y = t
print(x, y) #5  11

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items())) #[('Rolf', 96), ('Bob', 80), ('Anne', 100)]
# for student, attendance in student_attendance.itens():
#    print(f"{student}: {attendance}")

for t in student_attendance.items():
    print(t)
    print(f"{student}:{attendance}")
# ('Rolf', 96)
# ('Bob', 80)
# ('Anne', 100)

for student, attendance in student_attendance.items():
    print(t)
# ('Rolf', 96)
# ('Bob', 80)
# ('Anne', 100)

people =[("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"{"Name: {name}, Age: {age}, Profession: {profession}"}")

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession) # ageは不要のときアンダースコア Bob Mechanic

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(*tail)


# function
def hello():
    print("Hello World")

hello() # Hello World

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 364 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")

user_age_in_seconds()

friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name] # new variables only in the function scope
 # ERROR!!


def add_friend2():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name] # new variables only in the function scope
 # OK


friends = []
def add_friend3():
    friends.append("Rolf")

add_friend()
add_friend()
add_friend()
# ['Rolf', 'Rolf', 'Rolf']

print(friends) # [Rolf]

# Function arguments and parameter
def add (x, y):
    pass # Do nothing

add(5, 3)

def add (x, y):
    result = x + y
    print(result)

add(5, 3) # 8

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello("John", "Smith")
say_hello(surname="Smith", name="John")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You cannot divide")

divide(15, 0)
divide(dividend=15, divisor=0)


# Default parameter values
def add(x, y):
    print (x + y)

add(5, 8)

def add(x, y=8): # default value = 8
    print (x + y)

add(5)
add(x=5)


default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)


# Functions returning values
def add(x, y):
    print(x + y)
    return x + y

add(5, 8)
retult = add(5, 8)
print(result)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You cannot divide"

result = divide(15, 0)
print(result)


# Lambda function
def add(x, y):
    return x + y

print(add(5, 7))

lambda x, y: x + y
add = lambda x, y: x + y # can add new name
print(add(5, 7))

print((lambda x, y: x + y)(5, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 7]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))


# Dictionary comprehensions
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "rolf123"),
    (2, "Jose", "long4password")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping) #{'Bob': (0, 'Bob', 'password'), 'Rolf':(1, 'Rolf', 'rolf123'), 'Jose':(2, 'Jose', 'long4password')}
print(username_mapping["Bob"]) #(0, 'Bob', 'password')

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")


student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum(student['grades']) # total += sum(student['grades'])
        count = count + len(student['grades']) # count += len(student['grades'])
    return total / count


# Unpacking arguments
def multiply(*args): #*argsを使って任意の数の引数
    print(args)  # タプルとしての引数を表示
    total = 1 # 初期値を1に設定（掛け算のため）
    for arg in args:
        total = total * arg # 各引数を掛け合わせる
    return total

print(multiply(1, 3, 5))


def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))
print(add(**nums))


def apply(*args, operator): #*args: 任意の数の位置引数をタプルとして受け取ります。
    if operator == "*":
        return multiply(args) #operatorが "*" の場合、multiply 関数を呼び出します。
    elif operator == "+":
        return sum(args)    #operatorが "+" の場合、組み込み関数 sum を使用して引数の合計を計算します。
    else:
        return "No valid operator provided to apply()"

print(apply(1, 3, 6, 7), operator="+")


#関数に渡される引数をキーワード付きで渡すための方法です。kwargsは"keyword arguments"の略で、関数の引数として名前付きの値を指定する際に使います。
#kwargsは、通常、関数の引数リストで**（ダブルアスタリスク）を使って定義されます。これにより、関数は任意の数のキーワード引数を受け取ることができます。
def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25) # {'name': 'Bob', 'age': 25}


def named2(name, age):
    print(name, age)
details = {"name": "Bob", "age": 25}

named2(**details)


def greet(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}: {value}")

greet(name="Alice", age=30, country="USA")


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)

"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""