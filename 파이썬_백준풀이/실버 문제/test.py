#https://www.acmicpc.net/problem/2630

#재귀함수

def roop(length,y,x):

    global bule,white

    ch = [0,0]

    end_x = x+length 
    end_y = y+length

    # 정사각형 안에 지금 파란색 또는 흰색으로만 구성되어 있는지 확인
    for i in range(y,end_y):
        if 1 not in lists[i][x:end_x]:
                # 화이트
                ch[0]+=1
        elif 0 not in lists[i][x:end_x]:
                ch[1]+=1

    if ch[0] == length:
        white+=1
    elif ch[1] == length:
        bule+=1
    
    # 위조건에 안맞으면 완벽한 색종이가 아님 따라서 4분면으로 나눠서 재귀함수를 실행해준다.
    elif length != 1:
        
        # 2사분면으로 이동
        roop((length//2),y,x)

        # 1사분면으로 이동
        roop((length//2),y,x+(length//2))

        # 3사분면으로 이동
        roop((length//2),y + (length//2),x)

        # 4사분면으로 이동
        roop((length//2),y + (length//2),x+(length//2))

    return 0 
# 메인함수
length = int(input())
bule,white = 0,0
# 1 = 파란색 , 0 = 흰색
lists = [list(map(int,input().split())) for i in range(length)]

roop(length,0,0)

print(white)
print(bule)
