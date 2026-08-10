import re
pattern = r"\b[a-zA-Z]+[a-zA-Z0-9_.-]+[@][a-z]+[.][a-z]+\b"

with open("student_details","rt") as fh:
    data = fh.read()
match_obj = re.finditer(pattern,data)
for match in match_obj:
    print(match)
