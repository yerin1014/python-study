# 문자열
s = 'hello python'
print(s[6]) #인덱싱
print(s[6:12]) #슬라이싱

jumin = "080731-4199311"
print("성별: " + jumin[7]) #성별
print("월: " + jumin[2:4]) #월
print("일: " + jumin[4:6]) #일
print("뒷번호: " + jumin[7:]) #뒷번호
print("뒷번호: " + jumin[-7:]) #뒷번호

s1 = '나는 학생입니다'
s2 = '파이썬을 배웁니다'
s3 = '재밌습니다'
# 여러 줄 문자열, 입력한 그대로 저장
s4 = ''' 
    나는 학생입니다
    파이썬을 배웁니다
    재밌습니다
'''
print(s4)

year = '1980'
month = '02'
day = '13'
date = year + "-" + month + "-" + day
print(date)

date2 = date.split('-')
print(date2)   
print(type(date2))

print(date2[1][0:2], end = '*')

name = 'kakao taxi'
name2 = name.replace('k', 't', 1)
print()
print(name2)

print('python'*5) #반복

# 문자열에서 컴마 제거
won = '63, 120, 450'
won2 = won.replace(',', '')
print(won2)

won3 = 345908800
won4 = format(won3, ',')
print(won4)

#문자열 대소문자, 길이
p = 'Python is Amazing'
print(p.lower()) #소문자
print(p.upper()) #대문자
print(p.capitalize()) #첫 글자 대문자
print(p[0].isupper()) #true
print(len(p)) #길이
print(p.count('i')) #i의 개수

#위치
index = p.index('i') #7
print(index)
index = p.index('i', index + 1) #14
print(index)

#문자열 길이
words = ['Python', 'is', 'easy']
result = ' '.join(words) #' ' -> 사이에 공백 넣으면서 연결
print(result)

#제거
text = "   Hello    Python****"
print(text.strip()) #양쪽 공백 제거
print(text.rstrip('*')) #오른쪽 * 제거, .listrip(): 왼쪽 제거

#자리수만큼 0으로 채우기
num = '5'
result = num.zfill(3) 
print(result)

#format
age = 19
print("나는 %d살입니다." % age) #%d: 자리에 넣음
print("나는 {}살입니다.".format(age))

like = "노래부르기"
print("나는 %d살이고 %s를 좋아해요" %(age, like)) #%d: 숫자, %s: 문자열
print("나는 {0}살이고 {1}를 좋아해요".format(age, like))

#f 스트링
print(f"나는 {age}살이고 {like}를 좋아해요")

print('나의 주소는 {addr}이며, 나의 키는 {height}cm 입니다'.format(addr='인천', height=165))

# 이스케이프(탈출) 문자
print("\n배우는 과목은\n \"파이썬\"입니다.")
# \r : 커서를 맨앞으로 이동
print(" red apple\rpine") #\r은 맨앞으로
print("i like you!\b!!") # \b은 한 글자 삭제
print(" red\t apple")  # \t는 탭이동

p = 'Python is Amazing'
#인덱스 찾기
print(p.find('A')) #왼쪽부터 찾아서 인덱스 번호 출력, 10
print(p.rfind('A')) #오른쪽부터
print(p.index('a')) #왼쪽부터 찾아서 인덱스 번호 출력, 12
print(p.rindex('a')) #오른쪽부터

print(p.find('java')) #찾는 문자열이 없으면 -1
# print(p.index('java')) #찾는 문자열이 없으면 오류

arr_Str = input('Input String :').split('-')
#inforrmation.technology -> -기준으로 쪼갬 [0][1] 나누어서
arr_Len = int(input('Input Number : ')) #12
arr_Val = list(range(0, arr_Len,2)) #0 2 4 6 8 10
arr_Val.remove(4) #4 제거 -> 0 2 6 8 10
print(arr_Str[1].find('i')+arr_Val[2])
#technology에서 i 찾음 -> find 할 때 없으면 -1
# -1 + arr_Val[2] -> 6 = 5

