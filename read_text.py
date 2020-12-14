# open a file
myfile = open('myfile.txt')
# read all lines 
all_text = myfile.read()
# print out
print(all_text)

# reset the cursor
myfile.seek(0)

# read each line as a separate string in a list
lines = myfile.readlines()

print(lines)

