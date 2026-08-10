# regular expression (RegEx) - re module


import re
message = "The current python version is 3.13. other previous version are 3.12 ,3.11, 3.10."
"""
print("python" in message) # gives boolean result if it's there are not
print(message.find("python")) # gives index of the string
# strings methods or other data type methods not have pattern finding
# so we use ReEex for 
"""

"""
re.search(regex_pattern , string)
==> returns a match found , else returns NOne

"""
match_obj = re.search("[0-9][0-9]",message)
print(match_obj)

# metacharacters . matches any character  except new line character(\n)
match_obj = re.search("[0-9].[0-9][0-9]",message)
print(match_obj)