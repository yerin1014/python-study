a = int(input("투입할 돈"))
b = int(input("물건 값"))
c = a - b
print("거스름 돈:", c)
if ( c > 500 ):
    print("500원 동전의 개수:", c//500)
    c = c % 500
if ( c > 100 ):
    print("100원 동전의 개수:", c//100)
    print("나머지 금액:", c % 100)