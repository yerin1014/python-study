# 함수
def add(a, b): # () 안에는 매개변수
    return a+b

n1 = int(input("숫자1 입력"))
n2 = int(input("숫자 2 입력"))
# 함수 호출(인수) , 리턴값을 저장
sum = add(n1,n2)
print(sum)