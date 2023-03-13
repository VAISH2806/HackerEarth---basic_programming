
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
least = min(a)
count=0
for i in range(n):
    while((a[i]>least)):
        a[i]=a[i]-b[i]
        count+=1
    if(a[i]<least):
        least=a[i]
    if(a[i]<0):
        break
flag=True
for j in range(n-1):
    if(a[j]!=a[j+1]):
        flag=False
if(flag):
    print(count)
else:
    print(-1)
    


 

    



 
