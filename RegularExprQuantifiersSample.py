"""
Using quantifiers
"""

import re
str1 = "john: 1234567890, Merry:098, robert:234, Ruby:11100"

# get all phone numbers
print " All phone numbers: ", re.findall(r'\d+', str1)

# get all contact names
print " All phone names: ", re.findall(r'[a-zA-Z]+', str1)


# get all phone numbers with 10 digits
print " All phone names: ", re.findall(r'\d{10}', str1)

# get all contact names starting with  r
print " All phone names starting with r : ", re.findall(r'\b[rR][a-zA-Z]+', str1)

