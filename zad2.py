#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Birthday Cake Candles


import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max=candles[0]
    i=0
    while(i<len(candles)):
        if(candles[i]>max):
            max=candles[i]
        i=i+1
    return(candles.count(max))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')



Number Line Jumps


import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if(v1-v2!=0):
        if(((x2-x1)/(v1-v2)>0) and ((x2-x1)%(v1-v2)==0)):
            return ('YES')
        else:
            return ('NO')
    if(v1==v2):
        if(x1==x2):
            return('YES')
        else:
            return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()



Viral Advertising


import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    x=2
    y=2
    i=0
    while(i<n-1):
        x=x*3//2
        y=y+x
        i=i+1
    return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()



Recursive Digit Sum

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sd(s):
    if len(s) == 1:
        return int(s)
    result = 0
    for a in s:
        result += int(a)
    return sd(str(result))

def superDigit(n, k):
    result = 0
    for a in n:
        result += int(a)
    result *= k
    return sd(str(result))
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



Insertion Sort - Part 1


import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    k=arr[n-1]
    i=0
    while(i<len(arr)-1):
        if(k<arr[n-2-i]):
            arr[n-1-i]=arr[n-2-i]
            s=str(arr[0])
            j=1
            while(j<len(arr)):
                s=s+" "+str(arr[j])
                j=j+1
            print(s)
        else:
            break
        i=i+1
    arr[n-1-i]=k
    s=str(arr[0])
    j=1
    while(j<len(arr)):
        s=s+" "+str(arr[j])
        j=j+1
    print(s)
    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))







Insertion Sort - Part 2


import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for index in range(1, n):
        j = index
        while j > 0 and arr[j-1] > arr[index]:
            j -=1
        if j != index:
            arr.insert(j, arr[index])
            arr.pop(index + 1)
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


