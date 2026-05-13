import random
def get_lotto():
    numbers = []
    while len(numbers) < 6:
        n = random.randint(1, 45)
        if n not in numbers: # 포함하지 않냐
            numbers.append(n)
    return numbers # 6개의 숫자가 담긴 리스트 반환
print(f"로또 번호는 {get_lotto()} 입니다.")
# get_lotto 함수 호출 -> 빈 리스트 생성 