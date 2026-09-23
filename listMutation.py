def remove_list(lst):
	lst.pop()


original_list = [int(value) for value in input("Enter integers separated by spaces: ").split()]
print("Before:", original_list)

remove_list(original_list)

print("After:", original_list)
