s1 = {9,2,5,6}
s1.add(8)
print(s1,type(s1))
s2 = [2,35,7,8]
s2.insert(3,0)
print(s2)
s = {100, 3, 17, 1, 42}
print(s)

# frozen sets are -immutable sets
fs1 = frozenset({10,70,490,6})
print(type(fs1),fs1)

fs2 = frozenset({100,80,490,6})
print(type(fs2),fs2)
print(fs1.union(fs2))


