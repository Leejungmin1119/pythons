# 부모 노드를 찾는 함수 (경로 압축 적용)
man, party = map(int, input().split())

# 진실을 아는 사람의 정보 입력
a, *real = map(int, input().split())
real = set(real)
lists = []
ans = party
# 파티 인원수 입력
for i in range(party):
    
    lists.append(set(map(int,input().split()[1:])))

#진실을 아는 사람들이랑 같이 들은 사람들 입력

for i in range(man):
    for j in range(party):
        
        # 교집합의 값이 존재하는지 확인(있으면 이 파티는 진실을 말해줘야 된다..)
        if lists[j] & real:
            real = real.union(lists[j])  
            
for i in range(party):
    
    # 최종적으로 과장되어 말할 수 있는 파티의 갯수를 확인한다.
    if lists[i] & real:
        ans -=1

#출력
print(ans)