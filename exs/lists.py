#!/usr/bin/python3
# ### Lists
# python lists are ordered collection of heterogenious objects
l = [1, 2, 3]
print(l)
# #### _append() vs extend()_
# - append will add the object to end of the list it takes only one object
# - append will add the object as it is at end
# - extend will extend the list with passed iterable
# - extend will add the elements of the iterable passed to the list at end of
#   the list
# - if we extend list with dict only keys will be added to the list not values
# start
t = (40, 50, 60)
l.append([4, 5])
print('append a list to list', l)
l.extend([6, 7])
print('extend a list with list', l)
t = (20, 30)
l.append(t)
print('append a tuple to list', l)
l.extend(t)
print('extend a list with tuple', l)
d = {'first':1, 'secoend':2}
l.append(d)
print('append a dict  to list', l)
l.extend(d)
print('extend a list with dict ', l)
# end
# #### _remove() va pop()
# - remove() will remove the first occurence of the passed element
# - if nothing is found the an error will be raised
# - pop() will remove the last element of the list
# - pop() can remove the element based on the index if its passed
# start
print('REMOVE VS POP')
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(l1)
print('remove 10 from list')
l1.remove(10)
print(l1)
print('pop list')
l1.pop()
print(l1)
l1.pop(3)
print(l1)
