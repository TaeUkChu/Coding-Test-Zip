# https://school.programmers.co.kr/learn/courses/30/lessons/42840

answers= [1,2,3,4,5]

scores = [0]*3

student1 = [1,2,3,4,5]
student2 = [2,1,2,3,2,4,2,5]
student3 = [3,3,1,1,2,2,4,4,5,5]

students = [student1,student2,student3]

for student in students :
    multi = len(answers) // len(student)
    left = len(answers) % len(student)
    if multi == 0:
        student=student[:left]
    else:
        student*=multi
        student+=student[:left]

for i in range(3):
    for j in range(len(answers)):
        if students[i][j] == answers[j]:
            scores[i] += 1

max_score = max(scores)
answer = [i+1 for i, v in enumerate(scores) if v == max_score]
print(answer)