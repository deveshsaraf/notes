'''def sp(p,t,r):
    return p*t*r/100

print(sp(100,2,3,))


def welcome():
    print("hello wlecom")

welcome()

def add(x,y):
    return x+y
(add(20,30))
def welcome(name,phone,age=0,address=''):    (optional always at last)

def welcome(name,age,phone=""):
    print(f"hello to {name} ,your age is {age}{phone}")

(welcome("dev"))


def take_value(p,t,r):
    return [p,t,r]
def calculator():
    take_value(1,2,3)
    a=(p*t*r/100)

def display():
    calculator()



display()



def take_value():
    p=int(input("Enter the value of p:"))
    t= int(input("Enter the value of p:"))
    r = int(input("Enter the value of p:"))
    return [p,t,r]

def calculator():
    sp=take_value()
    return  sp[0] * sp[1] * sp[2] / 100
def display():
    print(f"the ans is {calculator()}")
display()

student=[
    ['rita','sita','hina','dina'],
    ['rama','shayama','mina','tina']
]
for x in student:
    print(x)

student=[
    ['rita','radha','hina','dina'],
    ['rama','shayama','gopal','tina']
]

x=0
while x< len(student):
    y=0
    while y<len(student[x]):
        print(student[0][1])
        print(student[1][1])
        exit()

def check_even_odd():
    numbers=int(input("Enter the number"))
    x=0
    while numbers%2==0:
        print(f'the even number are  {numbers}')
        x+=1
        exit()

    return


check_even_odd()
'''

def user_info():
    name=input("enter your name:")
    email=input("enter email:")
    phone=int(input('enter your number:'))
    return name,email,phone

print(user_info())


















