# a = "봄"
# b = "여름"
# print(a, b, sep = '과', end = '끝')
#sep: 변수 사이에 들어가는 것을 나타냄
#end: print문이 끝난 후에 들어가는 것을 나타냄

# for i in range(1, 100, 2) 1~99까지 2씩 증가하는 수열
# 구구단에서 원하는 단을 받아서 입력받아 출력

import time
a = int(input("몇 단을 출력할지 입력하세요."))
for i in range(1, 10): #1~9
    print(f"{a} x {i} = {a*i}")

for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} x {i} = {j*i}", end='\t') #\t: 탭 간격
    print() #줄바꿈

print()
for k in range(10, 0, -1):
    print(k)
    time.sleep(1)
print("발사!")