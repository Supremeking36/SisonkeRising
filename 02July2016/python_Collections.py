mylist=['Jessy','Brain','David','Vuyisile','Mandla','Suzan','Lesley']
print(mylist)

mylist.append('Maxwell')
print (mylist)

del mylist[2]
print(mylist)

mylist.append(1)
mylist[3]=100
print(mylist)

for i in mylist:
    print('Hello '+str(i))
