#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	new_li = my_list.copy()
	if(idx<0 or idx>len(my_list)):
		return new_li
	else:
		new_li[idx]=element
		return new_li