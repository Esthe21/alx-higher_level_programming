#!/usr/bin/python3

# element_at = __import__('1-element_at').element_at

def replace_in_list(my_list, idx, element):
	"""Replace an element of a list at a particular position."""
	if idx >= 0 and idx < len(my_list):
		my_list[idx] = element
	return (my_list)

