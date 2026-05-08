# a = input('주민번호를 입력하세요').split('-')

# if a[1][0] == '1' or a[1][0] == '3':
#     print("남자입니다.")
    
# elif a[1][0] == '2' or a[1][0] == '4':
#     print("여자입니다.")

#사용자로부터 세 개의 숫자를 입력받은 후
#가장 큰 숫자를 출력하라

num1, num2, num3 = map(int, input("세 개의 숫자 입력 : ").split(' '))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
elif num3 >= num1 and num3 >= num2:
    print(num3)