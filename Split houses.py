n=int(input())
grid = input()
grid=list(grid)
flag=1
for i in range(n-1):
    if(grid[i]=='H' and grid[i+1]!='.'):
        print('NO')
        flag=0
        break;

    if(grid[i]=='.'):
        grid[i]='B'
if(flag==1):
    print('YES')
    if(grid[n-1]=='.'):
        grid[n-1]='B'
    print(''.join(grid))


