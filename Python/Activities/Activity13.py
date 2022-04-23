from urllib.parse import _NetlocResultMixinStr


def getsum(numlist):
    a=0
    for i in numlist:
        a+=i
   
    return a
numlist = [10,40,50,60] 

test = getsum(numlist)
print(test)