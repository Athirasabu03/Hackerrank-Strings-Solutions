#!/usr/bin/env python
# coding: utf-8

# In[2]:


def swap_case(s):
    new_string=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            new_string.append(s[i].lower())
        elif (s[i].islower()==True):
            new_string.append(s[i].upper())
        else:
            new_string.append(s[i])    
        st=''
    return st.join(new_string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:




