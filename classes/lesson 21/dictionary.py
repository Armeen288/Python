testdict= {'codingal': 2, 'is': 2, 'best': 2, 'for':2, 'coding': 1}
print("The original dictionary:" + str(testdict))
k=2
res=0
for key in testdict:
    if testdict[key]==k:
        res=res+1
        print("frecuency of k is: "+ str(res))