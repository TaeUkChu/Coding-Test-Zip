# 문제 : https://www.acmicpc.net/problem/1181
# 정리 : https://velog.io/@uiseoo/%EB%B0%B1%EC%A4%80-%EB%8B%A8%EC%96%B4%EC%A0%95%EB%A0%AC%EC%8B%A4%EB%B2%845-1881

n = int(input())

words = []

for i in range(n):
    word = input()
    if word in words:
        pass
    else:
        words.append(word)

def selection(arr):
    n = len(arr)
    
    for idx in range(n-1):
        
        least = idx
        
        for i in range(idx+1, n):
            if len(arr[least]) > len(arr[i]):
                least = i                
                
            elif len(arr[least]) == len(arr[i]):
                if arr[least] > arr[i]:
                    least = i
                else:
                    least = least
                        
        arr[idx], arr[least] = arr[least], arr[idx]
    return arr

unique_li = selection(words)

for i in unique_li:
    print(i)


# words.sort() # 오름차순 -> 길이 기준으로 정렬하기 떄문에 x
# test = ['but','i','wont','hesitate','no','more','no','it']
# words = ['but','i','wont','hesitate','no','more','no','it','cannot','wait','im','yours']

