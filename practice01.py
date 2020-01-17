def d(n):
    st= str(n)
    sum = n
    for i in st:
        sum= sum+int(i)
    return sum

list=[]
n=1
x=0
while(1):
    x=d(n)
    if(x>9999):
        break
    else:
        list.append(x)
        n+=1
n=1
list.sort()
while(1):
    if n not in list:
        print(n)
    if n>=9993:
        break
    n+=1


# n=246
# st = str(n)
# len = len(str(n))
# sum = n
# for i in st:
#     print(i)
#     sum= sum+int(i)
#
# print(sum)