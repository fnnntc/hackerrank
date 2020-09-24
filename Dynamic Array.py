#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seqList=[]
    res=[]
    for i in range(n):
        S=[]
        seqList.append(S)
        #print(seqList)
    lastAnswer=0
    for q in queries:
        op, x,y = [int(i) for i in q]
        if op==1:
            Sn= (x^lastAnswer)%n
            #print("Sn={}".format(Sn))
            seqList[Sn].append(y)
        elif op==2:
            Sn= (x^lastAnswer)%n
            #print("Sn={}".format(Sn))
            #print("seqList={}".format(seqList))
            #print("y={}".format(y))
            #print("seqList[Sn]={}".format(seqList[Sn]))
            el=y%len(seqList[Sn])
            #print("val={}".format(val))
            lastAnswer=seqList[Sn][el]
            #print("lastAnswer={}".format(lastAnswer))
            res.append(lastAnswer)
    return res

#Query: 1 x y
#Find the sequence, , at index  in .
#Append integer  to sequence .


    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

