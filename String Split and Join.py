#!/usr/bin/env python
# coding: utf-8

# In[1]:


def split_and_join(line):
    s = line.split(" ")
    s= "-".join(s)
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:




