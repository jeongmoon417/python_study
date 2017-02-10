print 'This is list exercise'

#list exercise : this is my shopping list
shopping_list = ['apple', 'banana', 'milk']

print 'I have', len(shopping_list), 'items to purchase'

print 'These items are:',
for item in shopping_list:
    print item,
    # ',' avoids \n

shopping_list.append('rice')
print '\nMy shopping list is added rice and i \'ll show you my new list...', shopping_list

shopping_list.sort()
print 'This is sorted list..', shopping_list

old_item = shopping_list[0]
del shopping_list[0]
print 'I deleted first item:', old_item ,', so first item is changed, what is first itme?', shopping_list[0]

print '\n\nThis is tuple exercise'

#tuple exercise : zoo
#tuple : X have operations, canoot modify elements
zoo = ('python', 'elephant', 'snake', 'rabbit')
zoo2 = (2, ) #tuple has only one element
zoo3 =  'dog', 'cat', 'horse'

print 'Number of animals in the zoo is', len(zoo)
print 'zoo3', len(zoo3), ':', zoo3
#can i ommit "()"??

new_zoo = 'monkey', 'camel', zoo
print 'Number of cages in the new zoo is', len(new_zoo)
print 'All the animals in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[2][2]
print 'Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2])

print '\n\nThis is tuple exercise'

#dictionary exercise : address book

ab = { 'Jimin'  : 'jmin@python.com',
       'Minsu'  : 'min@python.com',
       'Jiyeong'    : 'jy@python.com',
       'Jangmi' : 'rose@python.com'
       }
print 'Jimin\'s address is', ab['Jimin']
print 'What is minsu\'s address?', ab.get('Minsu')

del ab['Jiyeong']
print 'After deleting jy\'s address, there are {} contacts in the address-book'.format(len(ab))

for name, address in ab.items():
    print 'Contact {} at {}'.format(name, address)

ab['Junsu'] = 'juns@python.com'
print 'New added address, Junsu\'s, is', ab['Junsu']

yes = False
print 'Is there Jangmi\'s address in address book?',
print 'Jangmi' in ab


