#Medina Kubanychbekova
#03/09/2025
# Problem 2 - Check sum comparison to 10
def sum_comparison():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    total = a + b
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is exactly 10.")