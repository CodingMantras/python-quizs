'''list.insert: Insert an item at a given position. 
The first argument is the index of the element before which to insert,
so a.insert(0, x) inserts at the front of the list,
and a.insert(len(a), x) is equivalent to a.append(x).

Therefore, If index >= length(list), it works as the list.append method 
and inserts at the end of the list.
'''

my_list = ['P', 'y', 't', 'h', 'o', 'n']
my_list.insert(100, "!")
print(my_list)
