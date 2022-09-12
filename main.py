# File Not found

# Basically, this architecture is used to ''catch'' errors in a way that it does not interrupt
# the execution of the code

# Try: you'll try to do things inside
# Exception: you'll do this if you found an error
# Else: if what you tried didn't give an error you'll execute this...
# Finally: This part of the code will execute no matter what
# Raise: You can raise your own errors

try:
    file = open("a_file.txt")
    a_dict = {"round": "a value"}
    print(a_dict["sss"])
except FileNotFoundError:
    file = open("a_file.txt", "a")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    raise ValueError
