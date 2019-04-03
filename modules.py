#import FileSample
# FileSample.readFromFile() # when we import the class Name without using from key word to access the methods we need to use the dot operator

from FileSample import readFromFile # no need to use the dot operator ie ClassName.method ie  FileSample.readFromFile()
readFromFile() # Directly calling the method . This we can do when we use the from keyword to import the class pointing to the method

from FileSample import writeToFile as wf # Using alias to refer to the method name
wf()

# if I want to import all the methods
from FileSample import *# imports all methods

readFromFile()
writeToFile()

