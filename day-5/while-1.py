# 1 ~ 100 까지 합과 개수
sum = 0
cnt = 0
i = 1

# 초기값
# while 조건 
while i <= 100:
    sum += i
    cnt += 1
    i += 1

print(f"합: {sum}")
print(f"개수: {cnt}")