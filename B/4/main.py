#!/bin/python

import pandas as pd;
import seaborn as sns;
import matplotlib.pyplot as plt;

if __name__=='__main__':
	my_cols=pd.read_csv('train.csv');
	pd.set_option('max_columns',None);
	#print('Initial Table-');
	#print(my_cols.head(20));
	my_cols.drop(axis=1,labels=['Cabin','PassengerId','Lname','Fname','SibSp','Parch','Fare','Ticket'],inplace=True);
	#print('\n\n');
	#print('After removal-');
	my_cols['Age'].fillna(20,inplace=True);
	my_cols['Embarked'].fillna('S',inplace=True);
	#print(my_cols.head(20));
	ax=sns.countplot(x='Pclass',hue='Survived',data=my_cols);
	ax.set(title='Passengers survived in each class',xlabel='Passenger Class',ylabel='Survived or Not');
	plt.show();
	ax=sns.countplot(x='Sex',hue='Survived',data=my_cols);
	ax.set(title='Passengers survived in each Gender',xlabel='Male or Female',ylabel='Survived or Not');
	plt.show();
	som_inter=(5,7,8,60,100);
	cat_s=['a','b','c','d'];
	my_cols['new_cat']=pd.cut(my_cols['Age'],som_inter,labels=cat_s);
	print(my_cols[['Age','new_cat']]);
