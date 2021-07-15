import re

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

