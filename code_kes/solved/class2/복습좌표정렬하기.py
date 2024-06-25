# 퀵정렬의 베이스코드(재귀함수)

def quick(arr):
    
    # 1. 종료조건
    # 리스트의 길이가 0이거나 1이면 이미 정렬된 상태이므로 그대로 결과를 반환
    if len(arr)<=1:
        return arr
    
    # 2. pivot 선정
    pivot=arr[len(arr)//2]
    
    # 3. left 구현, pivot 보다 작은 요소 값들
    left=[x for x in arr if x[0] < pivot[0]]
    
    # 4. right구현, pivot 보다 큰 요소 값들
    right=[x for x in arr if x[0] > pivot[0]]
    
    # 5. middle 구현, pivot과 값이 같은 값들
    # + 문제를 위한 추가 구현, middle로 저장된 값(= x좌표가 같은 값)들은 다시 y를 기준으로 정렬하여 작은 조건2를 만족하게 하였습니다.
    middle=[x for x in arr if x[0] == pivot[0]]
    middle.sort(key=lambda x : x[1])
    
    return quick(left)+middle+quick(right)
    
    
    
    
    
    