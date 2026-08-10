import copy

l1 = [1,23,4.6,[4,58,8],"py"]
# changes made to the inner copy element will change the original list
# shallow copy --it creates element at the different location but the inner elemnts are having same location
l2 = copy.copy(l1)
# print(l2)
# print((id(l1)))
# print((id(l2)))
# l1[3][0] =100
# l1[2]=10
# print(f"l1--{id(l1)} {l1}")
# print(f"l2--{id(l2)} {l2}")

# deep copy()
# nested elements will not change in the original 
l2 = copy.deepcopy(l1)
l1[3][0] =100
l1[2]=10
print(f"l1--{id(l1)} {l1}")
print(f"l2--{id(l2)} {l2}")