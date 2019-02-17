myDict = {0:'zero',1:'one',2:'two',3:'three'}
myList=list()
for key, val in myDict.items():
     myList.append(val,key)
x = myList[1]