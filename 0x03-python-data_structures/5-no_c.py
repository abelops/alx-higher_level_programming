#!/usr/bin/python3
def no_c(my_string):
	newString = ""
	for i in my_string:
		if(str(i)!="C" and str(i)!="c"):
			newString+=i
	return newString