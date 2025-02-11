def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be 0.")
        return
    
    return dividend / divisor

grades = [78, 99, 85, 100]

print("Welcome to the average grade program")

average = divide(sum(grades), len(grades))

print(f"The average grade is {average}")