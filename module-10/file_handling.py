# Opening a file in python
# open (file_name , mode_to_open)
# Modes: r , x , w, a , t , b
file_handler = open("practice.txt", 'r')
# x mode => create a file
fh = open("file2.txt",'wt')

# writing into a file
# write(content)
fh.write("have a good day!!")
# read()
content = file_handler.read(10)
print(content)
# readline() --- single line
line1 = file_handler.readline()
# readlines()---gives all lines
line2 = file_handler.readlines()
fh.close()
print(line1)
print(line2)

for line in line2:
    print(line.rstrip('\n'))