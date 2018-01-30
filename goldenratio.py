import sys
import random

def goldenRatioSimulator(a, b):
    count = 0
    divided = 0
    goldenRatio = 1.61803398874989484820
    originalA = a
    originalB = b
    while divided != goldenRatio:
        count += 1
        divided = b / a
        nextA = b
        b = a + b
        a = nextA
        # print a 
        # print b
        # print “[count]”
        # print count
        # print “[divided]”
        # print divided

    return {‘a’ : originalA, ‘b’ : originalB, ‘iter’ : count, ‘divided’ : divided}

group = []
for i in range(1, 10000):
    group.append(goldenRatioSimulator(float(random.randint(i, 100000)), float(random.randint(i, 100000))))




longestIter = 0
for x in range(1, len(group)):
   if(group[x][‘iter’] > longestIter):
       longestIter = group[x][‘iter’]
       longest = {
        ‘a’ : group[x][‘a’],
        ‘b’ : group[x][‘b’],
       
        ‘iter’ : longestIter,
         }

print longest (edited)