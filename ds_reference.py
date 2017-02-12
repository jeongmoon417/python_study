#Simple reference example#

print 'Simple Assignment'
shopping_list=['apple', 'banana', 'mango', 'strawberry']

mylist = shopping_list

del shopping_list[0]

print 'Shopping list is', shopping_list     #['banana', 'mango', 'strawberry']
print 'My list is', mylist      #['banana', 'mango', 'strawberry']

print 'Copy by making a full slice'
mylist = shopping_list[:]
del mylist[0]

print 'Shopping list is', shopping_list     #['banana', 'mango', 'strawberry']
print 'My list is', mylist      #['mango', 'strawberry']