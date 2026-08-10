# LIST IS A MUTABLE -->IT CAN BE CHANGED


student = ['annya', 6 , 85.02]
print(student)
days_of_week  = ["Mon" , "Tues" , " wed","THus" , "fri" , "sat"]
print(days_of_week[5])

# concatination of list
l1 = [1 , 2 , 3]
l2 = [4,5,6]
print(l1 + l2)

# * repeatation
print(l2 * 3)

# append()
# -->> adds an item to the end of the list

fruits = ["banana" , "apple" , "grapes" , "orange"]
print(fruits)
fruits.append("mango")
print(fruits)


# insert
# adds an element before the specified the specified index
# syntax : list.insert(index , item)
fruits.insert(2,"guava")
print(fruits)

'''
extend()
remove()
pop()
'''

# extend
subject = ["math" , "phy" , "social"]
subject.extend(["hindi" , "chemistry"])
print(subject)


# remove()
# it takes the element which has to be removed
subject.remove("social")
print(subject)

# pop() ==> it takes index of the element which has to be deleted
subject.pop(1)
print(subject)


"""
reverse()
sort()
count()
membership operation
"""
months = ["Jan " , "Feb" , "Mar" , "Apr" , "May"]
print(months)
# reverse()
months.reverse()
print(months)
#

# sort()
nums = list(map(int,input().split()))
# nums.sort(reverse=True)
print(nums)


#  count()
# print(nums.count(7))

# in  ,  not in
language = ['c' , 'py' , 'c++']
print('py' in language)
