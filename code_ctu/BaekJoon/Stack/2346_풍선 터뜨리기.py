'''
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고.
i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다.
단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다.
각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다.
이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다.
다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다.
양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다.
이동할 때에는 이미 터진 풍선은 빼고 이동한다.

예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자.
이 경우 3이 적혀 있는 1번 풍선,
-3이 적혀 있는 4번 풍선,
-1이 적혀 있는 5번 풍선,
1이 적혀 있는 3번 풍선,
2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.

예제 입력 1
5
3 2 1 -3 -1

예제 출력 1
1 4 5 3 2

2 1 -3 -1 -> (-3) -1 2 1 -> -1 2 1
-1 2 1 -> (-1) 2 1 -> 2 1
1 2 -> (1) 2
(2)


3 2 1 -3 -1
2 1 -3 -1 / 1,3
-1 2 1 / 4,-3
1 2 / 5, -1
1 / 2,2
3

'''
import sys
from collections import deque

N = int(input())
# 순서 + value 저장
deq = deque(enumerate(map(int,sys.stdin.readline().split(" ")),start=1))
first = True
result_list = []

while deq :

    #첫 번째 유무
    if first :
        jump = 0
        first = False
    else :
        jump = next
    deq.rotate(-jump)

    # jump가 양수/음수
    number = deq.popleft()
    if number[1] < 0:
        next = number[1]

    elif number[1] > 0:
        next = number[1]-1

    result = number[0]
    result_list.append(result)
    # print(deq,"번호",next,"결과",result,)

for result in result_list :
    print(result)

'''
import sys
from collections import deque

def balloons(N,deq):
    # N = int(input())
    # # 순서 + value 저장
    # deq = deque(enumerate(map(int,sys.stdin.readline().split(" ")),start=1))
    first = True
    result_list = []

    while deq :

        #첫 번째 유무
        if first :
            jump = 0
            first = False
        else :
            jump = next
        deq.rotate(-jump)

        # jump가 양수/음수
        number = deq.popleft()
        if number[1] < 0:
            next = number[1]

        elif number[1] > 0:
            next = number[1]-1

        result = number[0]
        result_list.append(result)
        # print(deq,"번호",next,"결과",result,)

    for result in result_list :
        print(result)
    return result_list

import unittest
class Test(unittest.TestCase):
    def test(self):
        input_N = 5
        input_nums = "-1 1 -1 1 -1"
        #input_nums = "3 2 1 -3 -1"

        input_list = deque(enumerate(map(int,input_nums.split(" ")),start=1))
        answer_list = [1,5,4,2,3]
        #answer_list = [1,4,5,3,2]
        self.assertEqual(balloons(input_N,input_list),answer_list)

if __name__=='__main__':
    unittest.main()

'''


