n=int(input())
array = list(map(int,input().split()))
length = len(array)
if(array[length-1]%10 != 0):
    print('No')
else:
    print('Yes')
