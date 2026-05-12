def dis_price(money, discount_rate):
    a = money *  discount_rate / 100
    return a



#a상품 가격: 10000원 할인율: 10
price_a = dis_price(10000, 10) #dis_price 함수명
print(price_a) #할인금액을 뺀 금액 출력

#b 상품 가격: 50000원 할인율: 20
price_b = dis_price(50000, 20) #dis_price 함수명
print(price_b) #할인금액을 뺀 금액 출력