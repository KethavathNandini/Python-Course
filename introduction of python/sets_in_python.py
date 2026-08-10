"""
sets are non-sequential - collections of items
comma separated elements enclosed within {}
===>> cannot have index in sets and slicing also not allowed
--->> sets do not allow duplicate elements
====>>> sets are mutable
===>> sets are unordered collection of unquie element
"""
set1 = {10, "python", 2.5, 10, 10}
print(set1)
print(len(set1))

# Membership operator  -in  ,not in
# add()
set1.add(20)
print((set1))
# remove()--->gives error if the element not present in set

set1.remove(10)
print(set1)
# discard()-->it does not give any error just prints the same set
set1.discard(30)
print(set1)
