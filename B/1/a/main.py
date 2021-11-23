#!/bin/python

def input_arr(n):
	mylist=[];
	for i in range(n):
		mylist.append(int(input('Enter integer element '+str(i+1)+' - ')));
	return mylist;

def dup_remove(some_list):
	return list(set(some_list));

if __name__=='__main__':
	n=int(input("Enter number of elements - "));
	if(n>0):
		mylist=input_arr(n);
		print('The enetered list is -');
		print(mylist);
		mylist=dup_remove(mylist);
		print('After removing duplicates -\n'+str(mylist));
		even_list=[x for x in mylist if(x%2==0)];
		print('List of even numbers -');
		print(even_list);
		print('Reversed list(no duplicates list)-');
		mylist.reverse();
		print(mylist);
	else:
		print('Wrong input!');
		exit();
