# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# 1. +와 -의 조합을 BFS로 결정
# 2. 조합의 순서를 결정

numbers=[4, 1, 2, 1]
target = 4

# 풀이 0 : 모든 경우의 수를 풀어서 계산
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# 풀이 1 : bfs를 활용한 방법
cnt = 0
li = [[0,0]] # index, cur_sum
while li :
    index, cur_sum = li.pop()
    if index == len(numbers) :
        if cur_sum == target:
            cnt+=1
    else:
        li.append([index+1,cur_sum+numbers[index]])
        li.append([index+1,cur_sum-numbers[index]])

print(cnt)


# 풀이 2 : dfs를 활용한 방법
def solution_dfs(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            if current_sum == target :
                return 1
            else :
                return 0
        # 현재 숫자를 더하는 경우와 빼는 경우로 나누어 재귀 호출
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    return dfs(0,0)
print(solution_dfs(numbers,target))