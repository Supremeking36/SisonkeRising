mylist=['Jessy','Brain','David','Vuyisile','Mandla','Suzan','Lesley']
#print(mylist)

#mylist.append('Maxwell')
#print (mylist)

#del mylist[2]
#print(mylist)

#mylist.append(1)
#mylist[3]=100
#print(mylist)

for i in mylist:
    print('Hello my name is '+str(i))

surlist= ['Sibitane','Kutu','Khoza','Masu','Mola','Seha']
print(mylist + surlist)

x=0
for n in range(len(mylist)-1):
    print('Hello I am '+ mylist[x]+' '+surlist[x] )
    x+=1
