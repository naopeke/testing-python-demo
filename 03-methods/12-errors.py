# def divide(dividend, divisor):
#     if divisor == 0:
#         print("Divisor cannot be 0.")
#         return   
#     return dividend / divisor

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
        raise TypeError
        raise ValueError
        raise RuntimeError
    return dividend / divisor

# grades = [78, 99, 85, 100]
grades = []

print("Welcome to the average grade program")

if len(grades) == 0:
    print("You don't have grades yet.")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list")
else:
    print(f"The average grade is {average}")
finally:
    print("Thank you")


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Mary", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades")
else:
    print("All student averages calculated")
finally:
    print("End of student average calculation")