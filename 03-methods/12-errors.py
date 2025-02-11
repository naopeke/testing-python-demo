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