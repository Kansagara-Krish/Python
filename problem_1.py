
#[4,6,5] [3,4,2] =[7,0,8]
'''
This code appears to solve the problem of adding two numbers that are represented as linked lists or arrays, where each element of the list represents a single digit of the number in reverse order
The result of summing 9999 + 65 would be 10064, which, when represented as a list in reverse order, is [4,6,0,0,1].
'''
print("-"*40)
print("This is addition 10-->0 add carry in next if it is less than 10 else add in it next one")
print("-"*40)
def addTwoNumbers(l1, l2):
    print("L1 is",l1)
    print("L2 is",l2)
    if len(l1)>len(l2):
        n=len(l2)    
    else:
        n=len(l1)
    l3=[]
    l=[]
    c=0
    for i in range(n):
        print(c)
        l3.append(l1[i]+l2[i])
        x= l3[-1]
        if x >= 10:
           a=int(x/10)
           x=x%10
           l.append(int(x+c))
           if c>0:
               c=c-1
           c=c+a
           
        else:
            y=int(l1[i]+l2[i]+c)
            if y >=10:
                a=y/10
                y=y%10
                y=int(y)
                l.append(int(y))
                if c>0:
                    c=c-1
                c=c+a

            else:
                y=int(y)
                l.append(int(y))
            
    if n==len(l1):
        for i in range(n,len(l2)):
            if l2[i]+c>=10:
                 c=int(l2[x]/10)
                 x=x%10
                 print(l2[x])
                 l.append(x)
    else:
        for i in range(n,len(l1)):
            if l1[i]+c>=10:
                l1[i]=l1[i]+c
                a=int(l1[i]/10)
                x=l1[i]%10
                l.append(x)
                if c>0:
                    c=c-1
                c=c+a
            else:
                l.append(int(l1[i]))
    if c!=0:
        l.append(int(c))
      
    print(l)


addTwoNumbers([9,9,9,7], [5,6,0,3])


'''
so the output is [4,6,0,1,1] reverse addition of [9,9,9,7] and [5,6,0,3]
7999+3065=11064
'''
