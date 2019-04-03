#list of ip separately
# list of port number


fp = open("ipAddress.txt")
lines = fp.readlines()

listOfIps = []
listOfPorts = []

for line in lines:
    print "line = ", line
    splits = line.split()
    ip = splits[0]
    if ip.count('.') == 3: # to validate ips have 3 dots 127.1.0.0
        listOfIps.append(splits[0])
    listOfPorts.append(splits[1])
print "Ips: ", listOfIps
print "Ports: ", listOfPorts

fp.close()

print "----- with statement : automatically closes no need to specifically say close()--- "
with open("ipAddress.txt") as fp:
    line = fp.readline()
    while line:
        print "line = ", line
        splits = line.split()
        listOfIps.append(splits[0])
        listOfPorts.append(splits[1])
        line = fp.readline()


