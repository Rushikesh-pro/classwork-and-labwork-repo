def palindrome(lst):
    return lst == lst[::-1]

my_list=[1,2,3,2,1]
if palindrome(my_list):
    print("The list {my_lsit} is a palindrome.")
else:
    print("The lst {my_lsit} is not palindrome.")


list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "cherry", "date"]

# Find the intersection
intersection = list(set(list1) & set(list2))

# Print the result
print(f"The intersection of the lists is: \n{intersection}")

