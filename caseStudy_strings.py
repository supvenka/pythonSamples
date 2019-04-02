logs = """This is error log #1
This is error log #2
This is error log #3
This is error log #4
This is error log #5
This is error log #6 err
This is error log #100 critical """

#no logs
# no of error logs with message , id
print "no of words logs = ", logs.count('log')
print "no of error logs = ", logs.count('error')

lines =  logs.split("\n")
for sentence in lines:
    print "Sentence = ", sentence
    if sentence.find("error") != -1:
        hashPos = sentence.find('#')
        spacePos  = sentence.find(' ', hashPos)
        if  spacePos == -1:
            id = sentence[hashPos + 1:]
        else:
            id = sentence[hashPos + 1: spacePos]
        print "ID = ", id




