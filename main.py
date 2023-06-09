try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message: # This helps you capture the error message and assign it to a variable
    print(f"The key {error_message} does not exist.")
else: # This code is ONLY executed if the 'try' code is executed and the 'except' code is not
    content = file.read()
    print(content)
finally:
    # Below we are creating or 'raising' our own custom error
    # The string we are passing as an arg is a 'custom error message'
    raise TypeError("This is an error that I made up.")

# Below we can leverage the 'raise' exception keyword to guide the users input

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)








