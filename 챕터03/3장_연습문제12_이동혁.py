'''
작성일 : 2023년 4월 4일
학과 : 컴퓨터공학부
학번 : 202395023
이름 : 이동혁
설명 : 연습문제 12
     사다리꼴의 넓이를 구하시오.
'''
# 1. 윗변을 입력 받아 정수로 변환하여 변수에 저장
top = int(input('윗변을 입력하시오 : '))

# 2. 아랫변을 입력 받아 정수로 변환하여 변수에 저장
bot = int(input('아랫변을 입력하시오 : '))

# 3. 높이를 입력 받아 정수로 변환하여 변수에 저장
hei = int(input('높이를 입력하시오 : '))

# 4. 사다리꼴 넓이를 계싼하여 변수에 저장
area = (top + bot) * hei / 2

# 5. 사다리꼴 넓이 출력
print("윗변 : {} 아랫변 : {} 높이 : {}" .format(top, bot, hei))
print("사다리꼴의 넓이는 {:.2f}입니다." .format(area))