'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395023
이름 : 이동혁
설명 : 현재 월을 입력 받아 계절을 출력하시오.
'''
# 1. 월을 입력받는다.
month = int(input('해당 월을 입력하시오 : '))

# 2. 만약 1~12월 사이라면
if month >=1 and month<= 12 :
    # 1.만약 3,4,5월 중 하나라면 봄출력
    if month >=3 and month <= 5 :
        print('봄입니다.')
    # 2. 만약 6,7,8월 중 하나라면 여름출력
    if month >= 6 and month <= 8:
        print('여름입니다.')
    # 3. 만약 9,10,11월 중 하나라면 가을출력
    if month >= 9 and month <= 11:
        print('가을입니다.')
    # 4. 아니라면 겨울출력
    else :
        print('겨울입니다.')
#아니라면 해당 월은 없습니다 출력
else :
    print('해당 월은 없습니다.')