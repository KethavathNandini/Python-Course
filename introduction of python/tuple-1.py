"""
while in list we can modify the list but not in tuple
Tuple() => sequance of items as acollection
 ==>> immutable
 ---->> tuples are used when there is no need to modify the data

"""
tup = ("n",10,5.78 , True , [1,2,3] , (2,3,4,5,"hello"))
print(len(tup))
print(tup[0:5:2])
tup = list(tup)
print(tup)
print(type(tup))

li = [1,2,4,5]
print(type(li))
li = tuple(li)
print(li,type(li))