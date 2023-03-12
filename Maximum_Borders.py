t=int(input())
for i in range(t):
    r,c = map(int,input().split())
    a=[]
    for val in range(r):
        value=input()
        a.append(value)
    ans=0
    for string in a:
        n=string.count('#')
        ans=max(ans,n)
    print(ans)
