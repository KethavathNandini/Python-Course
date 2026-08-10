'''
operation on strings ----> membership , strip , replace, count , start , end
'''

print("nandini "*3)
# membership operation
# ---->it checks whether the string present in another string --- using in,not in

s1 = 'python is fun'
print('python' in s1)
print('java' not in s1)

# comparison of strings--strip --->> to remove spaces
print('py'=='py')

# replace()
s2 = 'ppppython'
print(s2.replace('p','s',2))

# counting substring from a string
# count()
# string.count(substring)

str = "a good Habit leads to a good life"
print(str.upper().count('A'))


# changing case of a string
# upper() , lower() , title() ,capitalize()
print(str.title())
print(str.capitalize())

# staring and ending of a string
# startswith()
# string.startswith(substring)

print(str.startswith('A'))

# endswith()
print(str.endswith('life'))