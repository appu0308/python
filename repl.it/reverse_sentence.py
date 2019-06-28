''' To reverse sentence in right order Ex: Good Morning. Output: doog gninrom
https://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring?rq=1
'''
sentence=input("Enter the sentence to get reversed sentence: ")
reversed_sentence=sentence[::-1] 
# Used Slicing Technique- a string[::-1] to reverse string
temp=reversed_sentence.split() #used split for each word to copy to a temp list var
temp.reverse() #Reversed splitted temp list
reversed_list=list(temp) #copied reversed temp list using list()-python v3 function not v2
#Now we have to join the reversed list in reverse open
reversed_sentence=" ".join(reversed_list) #used "".join() to slice and merge the reversed list
print(reversed_sentence.lower()) #used lower() to change all words to lowercase.
