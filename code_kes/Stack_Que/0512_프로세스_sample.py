priorities = [1,9,9,1,8]
location = 0

answer = 0
loc = []

for i in range(len(priorities)):               ### priorities와 길이가 같아질때까지 반복하기 위한 장치
                                                ### 인덱스가 끝나도 처음 인덱스로 돌아가기 위함
    for i in range(len(priorities)):
        if max(priorities) == priorities[i]:   ### priority가 가장 높으면(max) 그 인덱스를 loc에 저장
            loc.append(i)                      ### 다음 최댓값을 위해 해당 인덱스의 밸류를 0으로
            priorities[i] = 0                  ### 그 다음 인덱스의 밸류가 최댓값이여도 바로 반영 가능

        if len(loc) == len(priorities):       # 현재 우선수위가 높은 우선순위가 아니면 면 넘어가고 
            break

    if len(loc) == len(priorities):            # 이중 for문이어도 break의 사용으로 모든 연산을 수행하지 않음.
            break    

answer = loc.index(location) + 1
    
print(answer)