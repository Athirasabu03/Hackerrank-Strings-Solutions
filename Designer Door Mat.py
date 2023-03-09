#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(int, input().rstrip().split()))
y=a[0]
x=a[1]
z=(x-7)//2
b=(y//2)+1
for i in range (1,y+1):
    if i==b:        
        print('-'*z+'WELCOME'+'-'*z)
    elif(i<b):
        print('---'*(b-i)+('.|.'*(i))+('.|.'*(i-1))+('---'*(b-i)))
    else:
        print(('---'*(i-b))+('.|.'*(y-i+1))+('.|.'*(y-i))+('---'*(i-b)))


# In[ ]:




