
print "User input till he provided correct /valid entry: Keep asking"
while True:
    data = raw_input("Enter a number") # raw inout is only a string
    if data.isdigit():
        print "Valid input", data
        break # breaks if user inputs a valid entry
    else:
        print "Invalid input", data
