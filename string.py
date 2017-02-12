name = 'jeongmoon'

if name.startswith('jeo'):
    print 'Yes, the string starts with "jeo"'

if 'a' in name:
    print 'Yes, it contains the string "a"'

if name.find('moon') != -1:
    print 'Yes, it contains the string "moon"'

delimiter = '--'
mylist = ['Brazil', 'Russia', 'India', 'Chana']
print delimiter.join(mylist)        #Brazil--Russia--India--Chana