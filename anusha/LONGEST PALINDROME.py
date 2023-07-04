CODE TO PRINT THE LONGEST PALINDROME IN THE LIST
-------------------------------------------
l=[121,12221,12,11]
freq={}
for i in l:
    i=str(i)
    if i in freq:
        freq[i]+=len(i)
    else:
        freq[i]=len(i)
new={}
for i,j in freq.items():
    new[j]=i
sorted=list(new.keys())
sorted.sort(reverse=True)
so={}
for j in sorted:
    so[new[j]]=j
print(so)
for i,j in so.items():
    temp=i
    n=int(temp)
    sum=0
    while(n>0):
        rev=n%10
        sum=sum*10+rev
        n=n//10
    count=0
    if(str(sum)==temp):
        count=count+1
    if count==1:
        print(i,"pal")
        break


OUTPUT:
{'12221': 5, '121': 3, '11': 2}
12221 pal
> 