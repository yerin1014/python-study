def calc(r1):
    result = 3.14 * r1 ** 2 #r1 반지름
    return result
r = float(input("원의 반지름 입력"))
area = calc(r)
print(area)
# print(result) #result는 함수 내부에서만 사용되는 지역변수이므로 에러 발생
########################
def calc2(r2): 
    global a #a는 전역변수로 선언
    a = 3.14 * r2 ** 2 #r1 반지름
    return a #지역변수

a = 0 #전역변수
rr = float(input("원의 반지름 입력"))
calc2(rr)
print(a) #0 전역변수



def function1():
    a = '이순신'
    c = [1, 2, 3]

   