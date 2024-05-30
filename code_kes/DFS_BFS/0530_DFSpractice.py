from collections import deque
number = [1,1,1,1,1]
target = 3
q =deque()
n = len(number) # 숫자배열의 크기


def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer