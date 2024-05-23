#Arithmatic Operator
a,b=6,2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print((2+4)*5-5*(4//2))     #Precedence of operators matters

#Assignment operator
a+=4
print(a)
#Now a becomes 10 a=10
a**=3
print(a)
#a=1000

#Relational Operators
print(a>20)
print(b!=2)

#Logical Operators
c=0
print(a>100 and b<100)
print(a>100 or b<100)
print(10 and 2)
print(not a)

#Bitwise operators
a,b=4,5
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>1)

#Identity Operators
x,y=2,2
print(a is b)
print(x is y)
print(x is not y)

#Membership operators
strn='Sneha Prajapat'
print('s' in strn)
print('s' not in strn)
print('Sneh' in strn)