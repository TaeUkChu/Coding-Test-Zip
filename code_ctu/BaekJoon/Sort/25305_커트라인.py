'''
2022 연세대학교 미래캠퍼스 슬기로운 코딩생활에 $N$명의 학생들이 응시했다.

이들 중 점수가 가장 높은 $k$명은 상을 받을 것이다.
이 때, 상을 받는 커트라인이 몇 점인지 구하라.

커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다.

입력
첫째 줄에는 응시자의 수 $N$과 상을 받는 사람의 수 $k$가 공백을 사이에 두고 주어진다.

둘째 줄에는 각 학생의 점수 $x$가 공백을 사이에 두고 주어진다.

출력
상을 받는 커트라인을 출력하라.

제한
- 1 <= N <= 1000
- 1 <= k <= N
- 0 <= x <= 10,000

예제 입력 1
5 2
100 76 85 93 98
예제 출력 1
98

Sol) 문제 접근 방식
1. 리스트를 내림차순 정렬
2. 인덱스 [k]를 찾는다.

Sol2) 사용할 알고리즘
1. 정렬 알고리즘 중 퀵정렬을 활용
2. python의 sort() 라이브러리 활용
'''

import sys
sys.setrecursionlimit(100000) #python recursion 깊이 설정
N,k = map(int,input().split())
scores = list(map(int,sys.stdin.readline().split()))
#1번 방법
def quick_sort(A):
    #종료 조건
    if len(A) <= 1:
        return A
    #pivot 설정
    pivot = A[0]
    tail = A[1:]

    left_side = [x for x in tail if x > pivot ]
    right_side = [x for x in tail if x <= pivot ]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
sorted_scores = quick_sort(scores)
print(sorted_scores[k-1])

'''
#2번 방법
sorted_scores = sorted(scores,reverse=True)
'''