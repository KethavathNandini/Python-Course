import re

s1 = "Python is a programming language . python3.13 "
# [A-Z], [a-z]
pattern = r"[A-Z][a-z]"
match_obj = re.search(pattern, s1)
print(match_obj)

# \d and \D
# \d matches 1 digit character . It is similar to [0-9]

pattern = r"[a-z][a-z][a-z]\d"
match_obj = re.search(pattern, s1)
print(match_obj)

# \D matches 1 non-digit character . It is similar to [0-9]
pattern = r"[a-z][a-z][a-z]\D"
match_obj = re.search(pattern, s1)
print(match_obj)

# \s , \S
# \s matches any whitespace character ,tab and new line as well
pattern = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pattern, s1)
print(match_obj)

# \S opposite of \s .It matches any character except ,space ,\n , \t
pattern = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pattern, s1)
print(match_obj)

# \w matches [A-Z] ,a-z] ,[0-9]
pattern = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pattern, s1)
print(match_obj)

# \W matches a character except [A-Z] ,a-z] ,[0-9]
pattern = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pattern, s1)
print(match_obj)

