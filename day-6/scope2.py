#파이썬은 변수를 찾을 때 가까운 영역부터 찾음
#LEGB 규칙(Local -> Enclosing -> Global -> Built-in)
#Local: 함수 내부에서 정의된 변수
#Enclosing: 함수 내부의 함수에서 정의된 변수
#Global: 모듈 수준에서 정의된 변수
#Built-in: 파이썬이 기본적으로 제공하는 함수나 변수
# 스코프(scope)
a = '홍길동' #전역 변수
b = 99 #전역 변수

def function1(): #함수1
    a = '이순신' #중첩함수 사용
    c = [1 ,2 ,3]
    
    def function2(): #함수1 안에 함수2
        d = (1, 2, 3)
        print('Local a =',a) #이순신
        print('Local b =',b) #99
        print('Local c =',c) #[1, 2, 3]
        print('Local d =',d) #(1, 2, 3)
        
    
    function2()
    print('Enclosing a =',a) #이순신
    print('Enclosing b =',b) #99
    print('Enclosing c =',c) #[1, 2, 3]
    # print('Enclosing d =',d) #d는 function2의 지역변수이므로 에러 발생
 
function1()
print('Global a =',a) #홍길동
print('Global b =',b) #99
# print('Global c =',c) #c는 function1의 지역변수이므로 에러 발생
# print('Global d =',d) #d는 function2의 지역변수이므로 에러 발생
