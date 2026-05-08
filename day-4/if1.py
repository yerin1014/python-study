# a = input("영어 한 글자 입력")
# if a.islower():
#     print("소문자입니다.")
#     print(a.upper())
# else:    
#     print("대문자입니다.")
#     print(a.lower())

#점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
#사용자로부터 score를 입력받아 학점을 출력하라.
#점수      학점
#81~100    A
#61~80     B
#41~60     C
#21~40     D
#0~20      E
score = int(input("점수 입력 : "))
if score >= 81 and score <= 100:
    print("A")
elif score >= 61 and score <= 80:
    print("B")
elif score >= 41 and score <= 60:
    print("C")
elif score >= 21 and score <= 40:
    print("D")
elif score >= 0 and score <= 20:
    print("E")
