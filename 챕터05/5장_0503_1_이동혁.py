'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395023
이름 : 이동혁
설명 : 사용자로부터 입력 받은 숫자에 해당하는 구구단을 출력하는 프로그램을 작성하시오.
'''
# 1. 단 입력받기
dan = int(input('단을 입력하시오 : '))

# 2. 곱하는 수를 1부터 9까지 반복하면서 :
for i in range(1,10) :
    # 1. 구구단 출력
    print('{} x {} = {}' .format(dan, i, dan * i))



#--------- while 문
# 1. 단 입력받기
dan2 = int(input('단을 입력하시오 : '))

# 2. 곱하는 수는 1부터
num = 1

# 3. 곱하는 수가 9까지:
while num <= 9 :
    # 1. 구구단 출력
    print('{} x {} = {}' .format(dan2, num, dan2 * num))
    
    # 2. 곱하는 수 1씩 증가
    num = num + 1
