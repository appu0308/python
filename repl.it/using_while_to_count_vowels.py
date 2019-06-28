#import reverse_sentence.py
s='tata consultancy services limited'
x = len(s) 
i = 0        
count = 0        
while (i < x):     
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':        
        count += 1        
    i = i+1        
print("Number of vowels: " + str(count))