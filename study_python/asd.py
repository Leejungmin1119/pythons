num,a =map(int,input().split())
arr = list(map(int,input().split()))
ans=0
sum=0

for i in range(num):
    sum+=arr[i]
    
    if sum >= a:
        ans+=1
        
print(ans)