def max_of_two(a: int, b: int) -> int:
    return a if a > b else b


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

print(max_of_two(num1, num2))