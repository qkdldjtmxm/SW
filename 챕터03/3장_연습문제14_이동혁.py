'''
작성일 : 2023년 4월 4일
학과 : 컴퓨터공학부
학번 : 202395023
이름 : 이동혁
설명 : 연습문제 14
        5과목 평균을 구하시오.
'''

# 1. 국어점수를 정수로 변환하여 입력 후 score1에 저장
score1 = int(input('국어 점수를 입력하시오 : '))

# 2. 수학점수를 정수로 변환하여 입력 후 score2에 저장
score2 = int(input('수학 점수를 입력하시오 : '))

# 3. 영어점수를 정수로 변환하여 입력 후 score3에 저장
score3 = int(input('영어 점수를 입력하시오 : '))

# 4. 사회점수를 정수로 변환하여 입력 후 score4에 저장
score4 = int(input('사회 점수를 입력하시오 : '))

# 5. 과학점수를 정수로 변환하여 입력 후 score5에 저장
score5 = int(input('과학 점수를 입력하시오 : '))

# 6. 5과목의 총합을 구하고 변수 sum에 저장
sum = score1 + score2 + score3 + score4 + score5

# 7. 5과목의 평균을 계산하여 변수 avg에 저장
avg = sum / 5

# 8. 총점과 평균을 출력
print("국어 : {} 수학 : {} 영어 : {} 사회 : {} 과학 : {}" .format(score1, score2, score3, score4, score5))
print("총점은 {}점 입니다." .format(sum))
print("평균은 {:.2f}점 입니다." .format(avg))