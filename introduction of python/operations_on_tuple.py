'''
concatination , repetation , memership
count , index
min ,max , sum
'''
from simple_intrest import p

std1 = (100, "richard")
std2 = (100, 67, 89, 85.09)
std = std1 + std2
print(std)

# index()--->for string ,tuple ,list
l1 = [1, 2, 3, 4]
print(l1.index(4))
str = "enjoy the journey"
print(str.replace("enjoy","good"),id(str))
print(str.index(" "))
print(str,id(str))
print(std2.index(89))
l2 = [4,7,2,7,9]
print(id(l2))
l2[2]=10
print(id(l2),l2)
p


# id