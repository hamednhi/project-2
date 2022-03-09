#Notice Enter username as String and Age integer
#Part of input name & age
UsersList=[]
Count_of_Members=int(input('Enter users count: '))

for i in range(Count_of_Members):

	dict1={}
	dict1['name']=input('Enter UserName: ')
	dict1['age']=int(input('Enter UserAge: '))
	UsersList.append(dict1)

#Part of Search

name=input('Enter name to search: ')
palse=False
for j in range(Count_of_Members):
	if UsersList[j]['name']==name:
		palse=True
		temp=j
if palse==True:
	print(UsersList[temp]['age'])
else:
	print('there is no user with given name!')
