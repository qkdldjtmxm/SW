'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395023
이름 : 이동혁
설명 : 실습예제 7-1
'''
import random
# 1. 비어있는 세트 2개 만들기
set1 = set()
set2 = set()

# 2. 랜덤으로 2개의 세트에 각각 10개의 값 저장.
#   랜덤, 반복하면서 (10번)
#       1)값 저장(추가)
for i in range(10) :
    set1.add(random.randint(1,10))
    set2.add(random.randint(1,10))
# 3. 2개의 세트 값 출력
#   합집합, 교집합, 차집합 출력
print('세트 set1 내용 : ', set1)
print('세트 set2 내용 : ', set2)
print('set1과 set2의 합집합', set1 | set2)  # | 은 합집합
print('set1과 set2의 교집합', set1 & set2)  # & 은 교집합
print('set1과 set2의 차집합', set1 - set2)  # - 은 차집합