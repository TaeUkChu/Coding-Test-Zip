# https://school.programmers.co.kr/learn/courses/30/lessons/42748

# 1. i부터 j까지 인덱싱 후 리스트로 저장
# 2. 새로운 리스트의 인덱스 return

def find_K(arr, command):
    i = command[0]
    j = command[1]
    k = command[2]

    new_li = arr[i-1:j]
    new_li.sort()
    print(new_li)
    return new_li[k-1]
arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
for command in commands :
    answer.append(find_K(arr,command))

print(answer)