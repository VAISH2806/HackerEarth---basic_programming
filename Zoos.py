string = input()
flag=True
for i in range(len(string)):
    if(string[i]=='z' or string[i]=='o'):
        flag=True
    else:
        falg=False
if(flag):
    z_count = string.count('z')
    o_count = string.count('o')
    if(o_count == 2*z_count):
        print('Yes')

    else:
        print('No')
            
    
