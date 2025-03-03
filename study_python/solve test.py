import heapq
def BFS(A):
    global N,M
    
    que = [A]
    
    while que:
        check_list = heapq.heappop(que)
        
        for i in bus[check_list]:# i = 버스의 도착지
            ch = value_list[1][check_list] + value_list[check_list][i]
            if value_list[1][i] > ch:
                
                value_list[1][i] = ch
                heapq.heappush(que,i)
#메인함수

N = int(input())# 지점 갯수
M = int(input())# 버스 위치
bus = {i : [] for i in range(N+1)}
value_list = [[float('inf')] * (N+1) for i in range(N+1)]
for i in range(M):
    start,end,value = map(int,input().split())
    
    
    value_list[start][end] = value# 비용 정보 저장
    value_list[end][start] = value
    
    bus[start].append(end)# 버스 정보 저장
    bus[end].append(start)


start_point,end_point = map(int,input().split())

BFS(start_point)

print(value_list[start_point][end_point])   