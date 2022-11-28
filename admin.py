'''user=input('Enter the user name:')
password=input("Enter the password:")
if user=="admin":
    if password=="admin123":
        print("welcome admin")
    else:
        print("Passowrd is incorrect")
elif password=="admin123":
    if user=="admin":
        print("welcome admin")
    else:
        print("User name is incorrect")
else:
    print("Both of them are wrong")
x=10
if x%2==0:
    print('even')
else:
    print("odd")

number=int(input('enter a number'))
if number%3==0 and number%5==0:
    print("it is can be divided by both number ")
else:
    print("sorry")

principal=int(input("Enter the amount"))
time=int(input("Enter the time"))
rate=int(input("Enter the rate"))
interest=principal*time*rate
print(interest)
interest_princial=interest/time*rate

print(interest_princial)


x=int(input('enetr first number:'))
y=int(input('enetr second number:'))
z=int(input('enetr third number:'))
if x>=y and x>=z:
    if y>=z:
        print(x,y,z)
    else:
        print(x,z,y)
elif y>=x and y>=z:
    if x>=z:
        print(y,x,z)
    else:
        print(y,z,x)
elif z>=x and z>=y:
    if x>=y:
        print(z,x,y)
    else:
        print(z,y,z)
else:
    print("all are same")
'''



