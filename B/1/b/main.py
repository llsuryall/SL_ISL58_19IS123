#!/bin/python

def count_words(my_string):
	my_string=my_string.split(' ');
	my_dict=dict.fromkeys(my_string,0);
	for word in my_string:
		my_dict[word]=my_dict[word]+1;
	return my_dict;

if __name__=='__main__':
	my_file=open('some.txt','r');
	my_str='';
	for each_line in my_file:
		my_str+=each_line.rstrip('\n');
	print(count_words(my_str));
