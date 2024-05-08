def solution(brown, yellow):
    answer = []

    # 규칙 0 : width > 3 , height > 3
    # 규칙 1 : (width+height)*2-4 = brown
    # 규칙 2 : (width-2)*(height-2) = yellow

    rule1 = int((brown+4)/2)
    print(rule1)

    for height in range(3,rule1-2):
        width = rule1 - height
        if (width-2)*(height-2) == yellow:
            return [width, height]

    return answer