n = input()
cnt = 0

for i in range(int(n)):
    words = list(input())
    word = words.pop()

    if len(words) % 2 == 0:
        cnt +=0 
    elif word != words[-1]:
        cnt +=0 
    elif word == words[-1] and word != words[-2]:
        cnt +=0
    elif word != words[-1] and words[-1] == words[-2]:
        cnt += 1
    else: cnt += 1
print(cnt)