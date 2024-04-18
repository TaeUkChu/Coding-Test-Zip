'''

// 내림차순 선택정렬

selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2 {
        A[1..last]중 가장 큰 수 A[i]를 찾는다
        if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    }
}

입력
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 10,000), 교환 횟수 K(1 ≤ K ≤ N)가 주어진다.

다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

출력
 K 번 교환이 발생한 직후의 배열 A를 한 줄에 출력한다. 교환 횟수가 K 보다 작으면 -1을 출력한다.

예제 입력 1
5 2
3 1 2 5 4

예제 출력 1
2 1 3 4 5
'''

import sys
input = sys.stdin.readline

N, K = map(int,input().split(" "))
# print(N,K)
# print(type(N),type(K))
array = list(map(int, input().split(" ")))
# print(array)

def selection_sort(array,K) :
    cnt = 0
    for i in range(len(array)) :
        max_indx = len(array)-1-i
        last = len(array)-1-i
        for j in range(last,-1,-1):
            if array[max_indx] < array[j] :
                max_indx = j
        if last != max_indx :
            array[max_indx],array[last] = array[last],array[max_indx]
            cnt+=1
        if cnt >= K :
            break
    if cnt < K :
        return -1
    return array

array = selection_sort(array,K)

if array != -1:
    for num in array :
        print(num, end=" ")
else :
    print(-1)
