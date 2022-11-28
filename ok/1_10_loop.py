'''x=1
names=[]
while x <=5:
    name=input('enter name')
    names.append(name)
    x +=1

for name in names:
    print(f'hello{name}')


data=[
    [12,13,14,15],
    [16,17,18,19],
    [20,21,22,23]
]

for a in data:
    for b in a:
        print(b)
    print("=========")

num_of_times=int(input("Enter number"))
increment=1
data=[]

while increment<=num_of_times:
    num=int(input("Enter another no"))
    data.append(num)

    increment+=1

rep_num=[]
for x in data:
    if data.count(x)>1 and x not in rep_num:
        rep_num.append(x)
for y in rep_num:
    print(f'{y} is rep {data.count(y)} times')
'''

#data=[1,2,3,3,4,4,2,2]
#data=['ram','gita','sita','ram','hari','sita']



