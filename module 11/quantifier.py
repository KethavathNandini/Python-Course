import re
message = "The current Python version is 3.13. other previous version are 3.12 ,3.11, 3.10."

pattern = r"[a-z]{4}"
match_obj = re.search(pattern,message)
print(match_obj)

pattern = r"[A-Z][a-z]{4}"
match_obj = re.search(pattern,message)
print(match_obj)

pattern = r"[A-Z][a-z]{4,5}"
match_obj = re.search(pattern,message)
print(match_obj)

# + ==> matches 1or more repetation  of the previous pattern
pattern = r"[A-Z][a-z]+"
match_obj = re.search(pattern,message)
print(match_obj)

# ? ==> matches 0 or 1 repetation  of the previous pattern
pattern = r"[A-Z][a-z]?"
match_obj = re.search(pattern,message)
print(match_obj)


# findall()
phones = "nan-1234567890, fay-6578390216, eran-9347687656, mikasa-873489"
patt = r"[0-9]{10}"
match_obj = re.findall(patt,phones)
print(match_obj)

phones = "nan-1234567890, fay-6578390216, eran-9347687656, mikasa-873489,python3.12,old-18 ,id-9"
patt = r"[0-9]+"
match_obj = re.findall(patt,phones)
print(match_obj)

# fetch all phone numbers, the phone numbers are exactly 7 digits and should not exceed 15

phones = "nan-1234567890, fay-6578390216, eran-9347687656, mikasa-873489,python3.12,old-18 ,id-9"
patt = r"[0-9]{7,}"
match_obj = re.findall(patt,phones)
print(match_obj)

# finditer()
patt = r"[0-9]{7,}"
match_obj_iter = re.finditer(patt,phones)
print(match_obj_iter)

for match in match_obj_iter:
    print(match)