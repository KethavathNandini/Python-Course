std1 = {
    'maths': 88,
    "eng": 90,
    "hindi":90,
    "chem":89

}
print(std1)
# get()
print(std1.get("phy",60))

# memership operator  ---> in ,not in ===> it checks the key not values

print('eng' in std1)

branch_1 ={
    "cse" : 300,
    "ece": 200,
    "eee": 100,
    "csbs": 156,
    "code":"sdes"

}
branch_2 ={
    "mpc" : 490,
    "bipc": 260,
    "eee": 120,
    "csbs": 100,
    "code":"sdgi"
}
# update() just updates the which is present and add if not there or if its new
branch_1.update(branch_2)
print(branch_1)
# pop()
branch_1.pop('cse')
print(branch_1)
'''
 keys  cannot be duplicated in dictionary
 not allowed keys-- set,dict (mutable)
 allowed keys -- string , int,float ,boolean,tuple (immutable)
'''

# values can be any datatype

student1 = {"id" :1008,"name":"john","markes":[2,5,6,7]}
print(student1["markes"][0])

# fetch the keys?
# keys()
print(student1.keys(),type(student1.keys()))
# values()
print(student1.values(),type(student1.values()))
# items() --- for fetching the pairs together
print(student1.items(),type(student1.items()))