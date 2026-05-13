from gugu_modul import *
while True:
    num = int(input("1.세로형 2.가로형 0.종료"))
    if num == 0:
        print("프로그램 종료")
        break
    elif num == 1:
        gugu_vertical()
    elif num == 2:
        gugu_horizontal()
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")