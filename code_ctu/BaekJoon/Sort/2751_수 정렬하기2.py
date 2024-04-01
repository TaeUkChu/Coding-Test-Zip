'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1
5
5
4
3
2
1

예제 출력 1
1
2
3
4
5

Sol) 접근 방식
- NlogN 시간 복잡도를 사용해야 함.
'''

import sys
N = int(sys.stdin.readline())
numbers=[]
for _ in range(N):
    numbers.append(int(sys.stdin.readline().strip()))
numbers.sort()
for number in numbers:
    print(number)

""" import sys
from collections import deque

N = int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(sys.stdin.readline().strip()))

def radixSort(nums):
    buckets = [deque() for _ in range(10)]

    max_val = max(nums)
    queue = deque(nums)
    digit = 1 # 자릿수

    while (max_val >= digit): # 가장 큰 수의 자릿수일 때 까지만 실행
        while queue:
            num = queue.popleft()
            buckets[(num // digit) % 10].append(num)
            # 각 자리의 수(0~9)에 따라 버킷에 num을 넣는다.

        # 해당 자릿수에서 버킷에 다 넣었으면, 버킷에 담겨있는 순서대로 꺼내와 정렬한다.
        for bucket in buckets:
            while bucket:
                queue.append(bucket.popleft())
        # print(digit,"의 자릿 수 정렬: ", list(queue))
        digit *= 10 # 자릿수 증가시키기
    return list(queue)
    # print(list(queue))
sorted_numbers = radixSort(numbers)
for number in sorted_numbers:
    print(number) """