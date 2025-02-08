#메인함수

import heapq

n = int(input())

#리스트 생성
lists = []


for i in range(n):
    for i in map(int,input().split()):
        #힙에다가 추가
        heapq.heappush(lists,i)

        #힙이 길이 n을 넘으면 최솟값을 pop
        if len(lists) > n:
            heapq.heappop(lists)

print(lists[0])