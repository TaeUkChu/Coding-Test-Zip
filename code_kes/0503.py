# 완전탐색-최소직사격형 정답코드
# 정리 : https://velog.io/@uiseoo/완전탐색-최소직사각형-Level-1

def solution(sizes):
    answer = 0
    
    width = []
    hight = []
    
    for i in sizes:
        width.append(i[0])
        hight.append(i[1])

    max_length = max(max(width), max(hight)) # 참고 코드1

    if max_length in width: # 참고 코드2
        for i in range(len(width)):
             if width[i] < hight[i]:
                width[i], hight[i] = hight[i], width[i]
                
        answer = max_length * max(hight)

    elif max_length in hight:
        for i in range(len(width)):
             if width[i] > hight[i]:
                width[i], hight[i] = hight[i], width[i]

        answer = max_length * max(width)

    return answer