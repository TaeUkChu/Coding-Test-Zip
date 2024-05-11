numbers = "011"
number = list(numbers)

answer = []


for i in range(len(number)):
    updeat_number = number[:i] + number[i+1:]
    self_chk = int(number[i])
    if self_chk == 2 or self_chk %2 != 0 and self_chk != 1:
        answer.append(number[i])
        
    for j in updeat_number: 
        PN = int(number[i]+j)
        if PN == 2 or PN%2 != 0 :
            answer.append(PN)