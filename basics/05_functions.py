def print_values(): 
    print("Hello, World!") 
    print("Welcome to Python functions.")
print_values()

def add_numbers(a, b):
    return a + b
print (add_numbers(5, 10))
def square(x):
    return x * x
print(square(4))
def is_even(num):
    if num % 2 == 0:
        print (f"{num} is even.")
    else:        print (f"{num} is odd.")
is_even(4)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0
print(convert_to_celsius(68))

def avg_list(numbers):
    return sum(numbers) / len(numbers)
print(avg_list([1, 2, 3, 4, 5]))