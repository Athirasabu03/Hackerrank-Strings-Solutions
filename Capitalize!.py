#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
import math
import os
import random
import re
import sys

def solve(s):
    return " ".join([name.capitalize() for name in s.split(" ")])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

