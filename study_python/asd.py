import sys
import heapq 

def BFS(A):
    
    lists = []
    #초기 가격값과 시작지점 저장
    heapq.heappush(lists,[value_result[start_p],start_p])
    
    while lists:
        v,s = heapq.heappop(lists)
        
        #만약 저장된 값보다 더 크면 돌릴필요가 없음
        if value_result[s] < v:
            continue
        
        for i in bus[s]:
            
            if value_result[i[1]] <= (v + i[0]):
                continue
            
            
            
            value_result[i[1]] = v+i[0]
            heapq.heappush(lists,[value_result[i[1]],i[1]])
        
N =int(sys.stdin.readline())#버스갯수
M =int(sys.stdin.readline())#노선갯수

bus = {i : [] for i in range(N+1)} # 노선을 저장하는 딕셔너리 변수

value_result = [float('inf') for i in range(N+1)]#가격

for i in range(M):
    #노선 정보 입력
    start,end,value = map(int,sys.stdin.readline().split())
    
    bus[start].append([value,end])
    
start_p,end_p = map(int,sys.stdin.readline().split())

#시작지점은 0
value_result[start_p] = 0

BFS(start_p)    
    
print(value_result[end_p])


# 1. 그냥 이중  for문이 아니라 그냥 1차원 배열로 넣어야 함.
# 2. while 문을 실행하고 나서 현재 내가 스타트 지점까지 오는데의 가격과 지금 저장되어 있는 최저 비용이랑 비교해야함 만약 false면 아래 함수는 무시한다.
#(왜 생기는가?) 그 변수들중 스타드 지점이 다른데 목적지가 같은 변수가 여려개 저장되어있다 치면 
"""
저장 [비용(10),5] 를 저장

하지만 다음에 변수는 [비용(3),5] 이러면

애초에 처음 변수 [10,5] 자체를 실행할 필요가 없어진다.
따라서 무의미한 시간소모가 되기에 따로 비교하는 if문을 구현해야 한다.

2. 그러면 작은 값이 나오면 그 값을 저장해야 하나?

필요없다. value_result[s]은 v보다 같거나 작다.
"""