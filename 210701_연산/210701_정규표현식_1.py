import re

txt = "The rain in Spain"
x = re.split("\s", txt);
print(x)

phone = "002-123-4567"
r = re.findall('^[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$', phone)
print(r)

txt = "02-123-4567"
txt2 = "02-1234-4567"

match_pattern = "\d{2}-\d{3}-\d{4}"
match_pattern_fulldigit = "\d{2}-\d{3,4}-\d{4}"

x = re.findall(match_pattern, txt)
print(x)

y = re.findall(match_pattern_fulldigit, txt2)
print(y)

y = re.findall(match_pattern_fulldigit, txt)
print(y)

txt = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"

match_pattern = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

x = re.findall(match_pattern, txt)
print(x)

ip = "192.168.130.12"
match_pattern = "^[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}[0-9]{1,3}$"
z = re.findall("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip);
print(z)
