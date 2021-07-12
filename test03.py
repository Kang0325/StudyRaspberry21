# Function

def min(a,b):
    if(a>b):
        return b
    else:
        return a

c=min(10,20)
print('10, 20 min value = {0}'.format(c))

def printS(c):
    print(c)

printS("hello")

def divide(a,b):
    return (a/b, a%b)

d,v=divide(4,2)
print(d,v)
print(type(d))