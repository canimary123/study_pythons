second = "Programming"
first = f"Welcome to Python Strings {second}"  # f-string

print(first)

first = "Hello Python"

# while first > 0:
#     print(first)
#     first = first - 1
#     문제점:

# first는 문자열(str) 타입: "Hello Python"
# while first > 0에서 문자열과 숫자를 비교하려고 시도
# Python에서는 문자열과 숫자를 >, < 같은 비교 연산자로 직접 비교할 수 없음

# 추가 문제:

# 설령 while문이 실행된다 해도 first = first - 1에서 문자열에서 숫자를 뺄 수 없어 또 다른 TypeError 발생

first = 5  # 문자열 대신 숫자로 변경

while first > 0:
    print(first)
    first = first - 1

   



    kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_all = sum(kor) + sum(eng)

print(f"총합: {sum_all}")


kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(0, 5):  # 0부터 4까지 (5번 반복)
    sum_total = sum_total + kor[i] + eng[i]

print(f"총합: {sum_total}")
