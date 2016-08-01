#!/usr/bin/env python

'''
Learning Python
2. Write a function that converts a list to a dictionary where the
index of the list is used as the key to the new dictionary (the
function should return the new dictionary).
'''


def list_to_dict(a_list):
	new_dict = {}
	for k ,v in enumerate(a_list) :
		new_dict[k] = v
		
	return new_dict
	
# Create a simple test list
test_list = range(100, 110)
test_list.append('whatever')
print test_list

# Call the function
test_dict = list_to_dict(test_list)
print test_dict
# Display the results
print
print "List: %s" % str(test_list)
print "Dict: %s" % str(test_dict)
print
	
