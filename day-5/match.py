# a = int(input("숫자를 입력하세요.(1: 입금, 2: 출금) "))

# match a:
#     case 1:
#         print("입금")
#     case 2:
#         print("출금")
#     case _:
#         print("잔액 없음")

num1 = int(input("3의 배수 입력: "))
num2 = int(input("5의 배수 입력: "))
match (num1 % 3, num2 % 5):
    case 0, 0:
        print("num1은 3의 배수, num2는 5의 배수")
    case 0, _:
        print("num1은 3의 배수, num2는 아무숫자")
    case _, 0:
        print("num1은 아무숫자, num2는 5의 배수")
    case _:
        print("둘 다 오류")