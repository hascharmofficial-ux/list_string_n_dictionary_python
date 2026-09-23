def change_string(s):
	s = "X" + s[1:]


original_string = input("Enter a string: ")
print("Before:", original_string)

change_string(original_string)

print("After:", original_string)
