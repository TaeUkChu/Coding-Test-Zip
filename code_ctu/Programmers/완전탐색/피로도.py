# https://school.programmers.co.kr/learn/courses/30/lessons/87946


"""
# 접근 방식 1
1. 소모 피로도 순으로 배열하기
2. 피로도 - 소모피로도 > 최소 필요 피로도 인 것만 남겨놓기

# 접근 방식 2
1. 소모 피로도 전체 합 < 피로도 이면 최소 피로도 기준
2. 최소 피로도 가장 높은 것 우선으로 제거
3. 남은 피로도 중 ...

# 접근 방식 3 : 완전탐색
1. while 피로도 > 소모 피로도 and
"""

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    index_li = [x for x in range(len(dungeons))]

    perm_set = list(permutations(index_li))
    answer_li = []
    for index_set in perm_set:
        answer = 0
        energy = k
        for index in index_set:
            dungeon = dungeons[index]
            if dungeon[0] <= energy:
                energy -= dungeon[1]
                answer+=1
        answer_li.append(answer)
    answer = max(answer_li)
    return answer


# dfs 풀이법
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
