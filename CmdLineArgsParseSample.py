"""
ArgsParseModule
"""
import argparse

# create parser
parserObj = argparse.ArgumentParser(description="This is a argsParse demo script")
parserObj.add_argument('-a', dest="fileName") # - optional argument with alias filename
parserObj.add_argument('-b', dest="noOfBytes", type=int) # - so optional argument alias is noOFbytes and type should be string
parserObj.add_argument('-c', default = False, help="is it a dir") # - so optional argument, but when not provided will take the default value = False also we provided a help for it

#Positional /Mandatory arguments : Order is mandatory
parserObj.add_argument('count', help="Some help", type=int)
parserObj.add_argument('units', help="either cms or meters")

args = parserObj.parse_args()
print "User supplied arguments = ", args
# print" Value of a = ", args.a ----use this only when no alias is provided
print" Value of a = ", args.fileName # when running the prog user will give value as -a but in our prog we need to access it as fileName
print" Value of b = ", args.noOfBytes
print" Value of c = ", args.c

#Accessing positional args
print" Value of count = ", args.count # positional arguments are refrred using the name we have given which is units
print" Value of units = ", args.units # positional arguments are refrred using the name we have given which is units