import re

txt = "192.168.0.1"
txt2 = "192.168.256.1"

match_pattern = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
match_precise_pattern = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
# if you want to it to be accurate,
# you need to check that the numbers are between 0 and 255,
# with the regex above accepting 444 in any position.
# You want to check for 250-255 with 25[0-5],
# or any other 200 value 2[0-4][0-9],
# or any 100 value or less with [01]?[0-9][0-9].
# You want to check that it is followed by a period \. three times {3}
# and then once without a period.

x = re.findall(match_pattern, txt)
print(x)

y = re.findall(match_pattern, txt2)
print(y)

x = re.findall(match_precise_pattern, txt)
print(x)

y = re.findall(match_precise_pattern, txt2)
print(y)
