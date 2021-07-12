#
n=1
name='Kang'
n=n+2
value=1.2*n

print('{0}=1.2*%{1}'.format(value,n))
print(name)

# String
greeting='Hello World'
print(greeting[0])
print(greeting[5:8])
print(greeting[:7])
print(greeting[-2:])
print(greeting*2)

# List
numbers=[0,1,2,3]
print(numbers)
print(numbers[0])
print(numbers[2:4])
names=['kim','kang','lee','park']
array=numbers+names
print(array)
print(array[-1])
print(array*2)
array[3]=7
print(array)

# Tuple
person=('kim',24,'male')
print(person)
print(person[1])
name1, age, gender = person
print(gender)