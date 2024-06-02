#numbers
"""#reverse
n=1234
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

#palindrome
n=1221
n1=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if rev==n1:
    print("it is palindrome")"""


"""#whether the digit is perfect or not
n=25
i=1
while i*i<n:
    i+=1
if i*i==n:
    print("perfect square")
else:
    print("not perfect")"""

"""#not perfect
n=27
i=1
while i*i<n:
    i+=1
if i*i==n:
    print("perfect square")
else:
    print("not perfect")"""

"""#check whether a number is power of 2
n=16
i=1
while i*2<n:
    i=i+1
if i*2==n:
    print("power of 2")
else:
    print("not")"""

"""#factorial
n=4
fact=1
while n>0:
    fact=fact*n
    n-=1
print(fact)"""

"""#fibonaci meanssum of last two numbers it starts with 0
n=4
fact=1
for i in range(1,n+1):
    fact=fact*1
print(fact)"""

"""n=5
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c"""

"""n=10
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c"""

"""#prime numbers
n=8
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
        print("prime")"""

"""n=7
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
        print("prime")"""
"""n=11
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
        print("prime")"""


"""n=21
for i in range(2,n//2):
    if n%i==0:
        print("not prime")
        break
else:
        print("prime")"""

"""import math as m
n=21
for i in range(2,int(m.sqrt(16))):
    if n%i==0:
        print("not prime")
        break
else:
        print("prime")"""

"""
#find the traversing in a list""

l=[1,2,3,4,5,0,8,9,4]
m=0
for i in range(len(l)):
    print(l[i])

l=[-1,-2,-3]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
print(m)
"""

#second largest 
""" 
l=[1,2,3,9,6,4,8]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
s=l[0]
for i in range(len(l)):
  if l[i]>s and l[i]!=m:
    s=l[i]
print(s)"""
"""
l=[8,7,6,5,4]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
s=min(l)
for i in range(len(l)):
  if l[i]!=m and l[i]>s:
    s=l[i]
print(s)"""

""" #imp
l=[1,1,1,1,1]
j=1
k=[]
i=0
while i<len(l):
    if l[i]==j:
        l.remove(j)
        continue
    i+=1
print(l)
        """





















































































