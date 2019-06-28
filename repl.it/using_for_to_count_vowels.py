'''Problem Statement
Consider the string 's' contains the value 'tata consultancy services limited'

Determine the no. of vowels present in it by using the "for" loop. Store the number in the variable 'count', and print it.
'''
s='tata consultancy services limited'
count=0
vowel=set('aeiou')
for letter in s:
  if  letter in vowel:
    count+=1
print(count)
