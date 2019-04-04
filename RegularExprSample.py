"""
Regular Expressions
"""
import re

data = "cat mat bat map that mapping"
pattern = r'm\w\w' # searches for m 3 characters including m ie m followed by any 2 alpha numeric chars

# option1 - compile (creates a compiled regex obj) and then search
regexObj = re.compile(pattern, re.IGNORECASE) # pattern = r'M\w\w' use IGNORE Case say we want to search for 'M'
matchObj = regexObj.search(data) # returns match obj or NONE # Searches for the first occurrance

if matchObj:
    print "First Occurrence", matchObj.group()
else:
    print "No match found"

#option2 - re.<method>() where we pass pattern and str to search in
matchObj = re.search(pattern, data) # case sensitive
if matchObj:
    print "First Occurrence of m :", matchObj.group()
else:
    print "No match found"

# match()
pattern = r'm\w\w' # searches for m in the beginning
matchObj = re.match(pattern,data) # Searching only at the beginning of the str: Here the str /data does not start with m
if matchObj:
    print "Search if the string starts with m :", matchObj.group()
else:
    print "String does NOT start with m"

# findall()
pattern = r'm\w\w'
listOfMatchObj = re.findall(pattern,data) # searches for all occurrances of m returns a list
print " All matches = ", listOfMatchObj

#split()
splittedList = re.split(pattern,data) #data = "cat mat bat map that mapping" so splits where it finds m note space also a char
# so cat<space>
# mat not considered since our pattern is m followed by 2 chars
# <space>bat <space>
# <space>that<space>
#ping
print "splitted list  = ", splittedList

#substitue for replacement
replaced = re.sub(pattern, "---", data)
print "replaced = ", replaced

