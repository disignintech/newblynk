def add_numbers(num1, num2):
    return num1 + num2

# function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

number1 = int(input("enter number :"))
number2 = int(input("enter number :"))

sum_result = add_numbers(number1, number2)
print("Sum is", sum_result)

product_result = multiply_numbers(number1, number2)
print("Product is", product_result)