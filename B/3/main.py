#!/bin/python3
from Reversed_Words import *;

if __name__=='__main__':
	my_line1=Reversed_Words(input("Enter line 1- "));
	my_line2=Reversed_Words(input("Enter line 2- "));
	my_line3=Reversed_Words(input("Enter line 3- "));
	som_ar=[my_line1,my_line2,my_line3];
	som_ar.sort(key=lambda my_line: my_line.vowel_count,reverse=True);
	for fg in som_ar:
		print(str(fg.sentence));
