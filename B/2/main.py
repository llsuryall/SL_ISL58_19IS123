#!/bin/python
import gc;
def print_menu():
	print(
'''Menu Options:
	c: Conversion
	p: Print history
	r: Clear history

Conversion input format:
	c 45 k
	# To convert from Celsius to Kelvin
	F 63 C
	# To convert from Fahrenheit to Celsius''');

def to_F(temp_k):
	return ((temp_k-273.15)*9/5)+32;

def to_C(temp_k):
	return temp_k-273.15;

def from_F(temp_f):
	return ((temp_f-32)*5/9)+273.15;

def from_C(temp_c):
	return temp_c+273.15;

def invalid_inp():
	print('Invalid Input!');
	return None;

def inp_temp():
	inp_str=input('Conversion string -\n-->');
	if not inp_str:
		return invalid_inp();
	try:
		inp_t=float(inp_str[1:-1]);
	except:
		return invalid_inp();
	if(inp_str[0]=='C' or inp_str[0]=='c'):
		from_temp='C';
		temp_k=from_C(inp_t);
	elif(inp_str[0]=='F' or inp_str[0]=='f'):
		from_temp='F';
		temp_k=from_F(inp_t);
	elif(inp_str[0]=='K' or inp_str[0]=='k'):
		from_temp='K';
		temp_k=inp_t;
	else:
		return invalid_inp();
	if(temp_k>=0):
		if(inp_str[-1]=='C' or inp_str[-1]=='c'):
			to_temp='C';
			co_temp=to_C(temp_k);
		elif(inp_str[-1]=='F' or inp_str[-1]=='f'):
			to_temp='F';
			co_temp=to_F(temp_k);
		elif(inp_str[-1]=='K' or inp_str[-1]=='k'):
			to_temp='K';
			co_temp=temp_k;
		else:
			return invalid_inp();
		return (inp_t,from_temp,co_temp,to_temp);
	else:
		return invalid_inp();

if __name__=='__main__':
	hist=[];
	print_menu();
	while(True):
		inp=input('Your Choice - ');
		if not inp:
			inp='0';
		if(inp=='c' or inp=='C'):
			temp_tup=inp_temp();
			if(temp_tup!=None):
				hist.append(temp_tup);
				print(str(temp_tup[0])+' '+temp_tup[1]+' = '+str(temp_tup[2])+' '+temp_tup[3]);
				del temp_tup;
		elif(inp=='p' or inp=='P'):
			if(len(hist)!=0):
				print('History - ');
				for item in hist:
					print(str(item[0])+' '+item[1]+' = '+str(item[2])+' '+item[3]);
			else:
				print('History is empty');
		elif(inp=='r' or inp=='R'):
			del hist;
			gc.collect();
			hist=[];
			print('History cleaned');
		elif(inp=='q' or inp=='Q'):
			del hist;
			gc.collect();
			print('Exiting...');
			break;
		else:
			invalid_inp();
		print();
