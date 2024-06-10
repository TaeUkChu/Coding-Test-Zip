# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 풀이
# 1 : 리스트를 내림차 순 정렬 후
# 2 : if i+1 >= arr[i] : True
def solution(citations):
    # citations =  [3,0,6,1,5]
    citations = sorted(citations,reverse=True)
    answer = 0
    for i in range(len(citations)):
        if citations[i] <= i+1 :
            answer = max(citations[i],i)
            break
        else: # 왜 이렇게 써져야 하는지 잘 모르겠음.
            answer = len(citations) 
    return answer

solution([3,0,6,1,5])