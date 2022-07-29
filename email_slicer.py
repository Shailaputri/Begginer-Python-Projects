"""Email Slicer"""

str_email = input("Enter mail id in format of username@domain:\t")
list_email = list(str_email)
for ele in list_email:
	if ele == '@':
		ind = list_email.index(ele)

#print(ind)
username = []
i= 0
while i<ind:
	username.append(list_email[i])
	i = i+1
#print("Your username is {}".format(''.join(username)))
domain= []
i = len(list_email)-1
while i>ind:
	domain.append(list_email[i])
	i = i-1
print("Your username is {} & domain is {}".format(''.join(username),''.join(domain[::-1])))