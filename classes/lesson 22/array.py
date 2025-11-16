import array as arr
arraynum=arr.array('i',[1,3,5,3,7,9,3])
print("original array:"+str(arraynum))
print("number of occurrences of the number 3 in the said array is: "+str(arraynum.count(3)))
arraynum.reverse()
print("reverse the order of the items: ")
print(str(arraynum))