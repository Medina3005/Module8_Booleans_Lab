#Medina Kubanychbekova
#03/09/2025
# Problem 3 - Check if 5 is in the list
def check_five():
    user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    if 5 in user_list:
        print("The number 5 is in the list.")
    else:
        print("The number 5 is not in the list.")