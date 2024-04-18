# 실패

'''
insertion_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for i <- 2 to N {
        loc = i - 1;
        newItem = A[i];

        # 이 지점에서 A[1..i-1]은 이미 정렬되어 있는 상태
        while (1 <= loc and newItem < A[loc]) {
            A[loc + 1] <- A[loc];
            loc--;
        }
        if (loc + 1 != i) then A[loc + 1] = newItem;
    }
}

입력
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 10,000), 변경 횟수 K(1 ≤ K ≤ N2)가 주어진다.

다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

출력
K 번 변경이 발생한 직후의 배열 A를 한 줄에 출력한다. 변경 횟수가 K 보다 작으면 -1을 출력한다.

예제 입력 1
5 7
4 5 1 3 2
예제 출력 1
1 3 4 5 5

'''

import sys
input = sys.stdin.readline

N,K = map(int, input().split(" "))
array = list(map(int, input().split(" ")))

def insertion_sort(array,K):
    cnt = 0

    for pivot_index in range(1,len(array)):

        isChange = False
        pivot = array[pivot_index]
        if cnt >= K :
            break

        for loc in range(pivot_index-1,-1,-1):
            if cnt < K :
                if pivot < array[loc]:
                    array[loc+1] = array[loc]
                    cnt+=1
                    isChange = True
                    cur = loc
                    print(array)

                if isChange :
                    array[cur] = pivot
                    cnt+=1
                    print("pivot 이 후",array)
                    break
    if cnt < K :
        print(-1)
        print(cnt)
    else :
        for num in array:
            print(str(num), end=" ")

insertion_sort(array,K)

        # if cnt >= K :
        #     break

        # while (0 <= loc and array[loc] > pivot and cnt < K):
        #     array[loc+1] = array[loc]
        #     loc-=1
        #     cnt+=1
        #     print(array)

        #     if cnt >= K :
        #         break

        # if (loc + 1 != i and cnt < K): # 위치가 pivot 위치와 같으면 안됨
        #     array[loc+1] = pivot
        #     cnt+=1
        #     print(array)

