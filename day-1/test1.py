name = input("상품 이름 입력")
price = int(input("가격 입력"))
count = int(input("수량 입력"))
total = price * count
print(name, "의 총 금액은", price*count)
print(name + "의 총 금액은 " + str(price*count))
print(f"{name}의 총 금액은 {total}")

# print 안에서 f 는 f-string 이라하며 포맷 문자열 -> f" {변수 값}   "
# 숫자 -> 문자로 변환: str
# 실수는 float만 있음 (8바이트)