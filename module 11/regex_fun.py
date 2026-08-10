import re

# findall()
phones = "nan-1234567890, fay-6578390216, eran-9347687656, mikasa-873489"
patt = r"[0-9]{10}"
match_obj = re.findall(patt, phones)
print(match_obj)

phones = "nan-1234567890, fay-6578390216, eran-9347687656, mikasa-873489,python3.12,old-18 ,id-9"
patt = r"[0-9]+"
match_obj = re.findall(patt, phones)
print(match_obj)

# fetch all phone numbers, the phone numbers are exactly 7 digits and should not exceed 15

phones = "nan-1234567890, fay-6578390216, eran-9347687656, mikasa-873489,python3.12,old-18 ,id-9"
patt = r"[0-9]{7,}"
match_obj = re.findall(patt, phones)
print(match_obj)

# finditer()
patt = r"[0-9]{7,}"
match_obj_iter = re.finditer(patt, phones)
print(match_obj_iter)

for match in match_obj_iter:
    print(match)

# substituting the pattern - sub()
s1 = "Sunday , Monday, Tuesday ,Monday, Sunday, Sunday,Saturady"
result = re.sub(r"S[a-z]+", 'Wednesday', s1)
print(result)

message = """ We  are learning re. using RE, we can 
search for a pattern in a given string using the sub(), 
we can replace the pattern with a given string as welll
"""
patt = r"\bre\b"
match_obj = re.sub(patt ,"Regular Expression",message, flags=re.IGNORECASE)
print(match_obj)