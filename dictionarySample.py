"""
Dictionary Sample
"""
contacts = {'john':123}
print "contacts = ", contacts

print "-- Adding ---"
contacts['merry']= 987
print "contacts = ", contacts

print "-- updating dict ---"
contacts['john']= 345
print "contacts = ", contacts

print "-- Key value ---"
print "phone number of contacts[merry] = ", contacts['merry']


# print "phone number of contacts['not present'] = ", contacts['not present'] #KeyError: 'not present' Program terminates
print "Ruby phone number contacts['not present'] =  ", contacts.get('not present') # gives None : prog does not terminate
print "provide Default Value when key not present = Ruby phone number contacts['not present'] =  ", contacts.get('not present', 100 ) # gives the provided default value

if 'Ruby' in contacts:
    print "Ruby's number = ", contacts['Ruby']
else:
    print "No contact for Ruby"


print "-- Adding dict to dict--- Merging"
officeContacts = {"Robert" :787, "john":111, 'Mike':333}
contacts.update(officeContacts)
print "contacts = ", contacts # johns gets overriden

friends = ['abc', 'xyz']
friendsContacts = dict.fromkeys(friends) # no values for the keys
print "friendsContacts = ", friendsContacts
friendsContacts = dict.fromkeys(friends, 500) # Providing a default value
print "friendsContacts = ", friendsContacts

mydict = {'john': [100,111,222]}
print mydict['john']
mydict['john'].append(987)
print mydict['john']

officeContacts = {"Robert" :787, "john":111, 'Mike':333}
print "Total contacts = ", len(officeContacts)

print "Contact Names"
for key in officeContacts:
    print "Key = ", key

print "Contact Names"
for key in officeContacts.keys(): # Using keys() same as above
    print "Key = ", key



print "Phone number only"
for value in officeContacts.values(): # Using keys() same as above
    print "value = ", value

print "Both keys and Values"
for key, value in officeContacts.items():
    print "Key = ", key , " Value = ", value


# officeContacts.['john'] = [123, 567]
officeContacts['john'] = {'mobile':123, 'landline':80} # This way we can differentiate john mobile and lan this is dict key with dict value
print "officeContacts.['john'] = ", officeContacts['john']
print "officeContacts['john']['landline'] = ", officeContacts['john']['landline']

#pop
removed = officeContacts.pop('Robert')
print "removed = " , removed
print "officeContacts = " , officeContacts

# Remove all values
officeContacts.clear()
print "officeContacts = " , officeContacts

