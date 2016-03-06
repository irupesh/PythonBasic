
key=int(input())
temp=int(key/5)
zero=0
power=1
while(temp>0):
    zero=zero+temp
    power+=1
    temp=int(key/(5**power))
print(zero)