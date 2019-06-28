#import reverse_sentence.py 
'''Problem Statement
Write a script that performs the following tasks serially:

Create an empty list 'emplist1' using list operation.
Print 'emplist1'.
Append to empty list 'emplist1' created above with element 9.
Append another element 10 to 'emplist1'.
Print 'emplist1'.
Create an empty list 'emplist2' using [].
Print 'emplist2'.
Extend the empty list 'emplist2' created above with elements 'a', 'b', 'c'.
Print 'emplist2'.
Remove the last element of 'emplist2', and assign it to variable 'e'.
Print 'emplist2'.
Print the variable 'e'.
'''
emplist1=[]
print(emplist1)
emplist1.append(9)
emplist1.append(10)
print(emplist1)
emplist2=[]
print(emplist2)
emplist2.append('a')
emplist2.append('b')
emplist2.append('c')
print(emplist2)
emplist2.remove('c')
emplist2.append('e')
print(emplist2)




'''Problem Statement
Write a script that performs the following tasks serially:

Create an empty tuple 'tup1' using tuple operation.
Print 'tup1'.
Create another tuple 'tup2', by passing 'Welcome' string as argument to tuple function.
Print 'tup2'.
Find and print the count of character 'e' in 'tup2'.
Determine the index of character 'e' in 'tup2' and print it.
Find the length of tuple 'tup2' and print it.
'''
'''
tup1=tuple()
print(tup1)
tup2=tuple('Welcome')
print(tup2.index('e'))
print(len(tup2))'''
