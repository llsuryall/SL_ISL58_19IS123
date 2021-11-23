#!/bin/python3
def input_arr():
	n=int(input('Enter number of elements for integer array - '));
	mylist=[];
	for i in range(n):
		mylist.append(int(input('Enter integer element '+str(i+1)+' - ')));
	return mylist;

def Max(my_list):
	if len(my_list)==1:
		return my_list[0];
	else:
		m=Max(my_list[1:]);
		return m if m>my_list[0] else my_list[0];

if __name__=='__main__':
	some_arr=input_arr();
	print('Max element is - '+str(Max(some_arr)));
