#!/bin/python

my_f=open('som.txt','r');
l_lines=my_f.readlines();
txt='';
for some_l in l_lines:
	some_l=some_l[:-1];
	txt+=some_l;
txt=txt.split(' ');
my_word_dict=dict.fromkeys(txt,0);
for word in txt:
	my_word_dict[word]+=1;
del my_word_dict[''];
sorted_di=sorted(my_word_dict,key=lambda item:my_word_dict[item],reverse=True);
i=0;
print('Maximum occurrence words in descending order -');
my_lis=list();
for word in sorted_di:
	print(word);
	my_lis.append(len(word));
	i+=1;
print();
print('List of length of words -');
print(my_lis);

print('Average length of words is '+str(sum(my_lis)/len(my_lis)));
print('Square of lengths is -');
print([x*x for x in my_lis]);
