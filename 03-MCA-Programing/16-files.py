# Opening text file.
file = open("example.txt", "r")

# Reading text file.
content = file.read() # reads the whole file and returns all lines
print(content)

file.seek(0)
line = file.readline() # reads a single line and returns a single line
print(line)

file.seek(0)
lines = file.readlines() # reads all line and returns list of all lines
print(lines)

file.close()

# Writing to text file.
file2 = open("example.txt", "w")
file2.write("Writing to text file")
file2.close()

# specify character encoding.
with open("example.txt", "r", encoding="utf-8") as file: 
    content = file.read()
    print(content)

# write to a text file.
items = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as file:
    for item in items:
        file.write(f"{item}\n")

# append to a text file.
with open("fruits.txt", "a") as file:
    file.write("orange\n")

# read to a text file.
with open("fruits.txt", "r") as file:
    for line in file:
        print(line.strip())

# write to a binary file.
data = b'\x00\xFF\x00\xFF'  # Sample binary data 
with open('binary.dat', 'wb') as file: 
    file.write(data) 

# append to a binary file
new_data = b'\xDE\xAD\xBE\xEF' 
with open('binary.dat', 'ab') as file: 
    file.write(new_data)

# read to a binary file.
with open('binary.dat', 'rb') as file: 
    data = file.read() 
    print(data) 

# read and write file.
with open("new_file.txt", "w+") as file:
    file.write("i love python programming language")
    file.seek(0)
    content = file.read()
    print(content)

# multiple file operation using with statement.
with open('image.jpg', 'rb') as source, open('copy_image.jpg', 'wb') as dest: 
    data = source.read() 
    dest.write(data)

