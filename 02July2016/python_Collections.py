mylist=['Jessy','Brain','David','Vuyisile','Suzan','Lesley']
#print(mylist)

#mylist.append('Maxwell')
#print (mylist)

#del mylist[2]
#print(mylist)

#mylist.append(1)
#mylist[3]=100
#print(mylist)

#for i in mylist:
#    print('Hello my name is '+str(i))

surlist= ['Sibitane','Kutumela','Khoza','Masuku','Mola','Sehata']
#print(mylist + surlist)
agelist=[12,32,4,13,45,22,21]

collist=['Blue','Green','Red','Pink','White','Black']


for a,b,c,d in zip(mylist,surlist,agelist,collist):
    print('Hello I am {0} {1}, im {2} years old and my favourate colour is {3}'.format(a,b,c,d)
          )

