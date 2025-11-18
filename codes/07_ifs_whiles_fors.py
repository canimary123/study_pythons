# 중급 난이도 문제 1 — 문자열과 f-string 활용
# second 문자열에 "Python"이 포함되어 있는지 확인하고,
#  "Welcome!"과 합쳐서 출력하는 코드를 작성하시오.
# 조건: f-string 사용


# 출력 예시: "Welcome! Python is fun"


# second = "Python"
# # 여기에 코드 작성

# second = "Python is fun"

# output = f"Welcome! {second}"

# print(output)

# ✅ 중급 난이도 문제 2 — while 반복문 응용
# first 변수가 5부터 1까지 감소하도록 while문을 작성하고,
#  first == 2일 때만 "special"을 출력하도록 코드를 작성하시오.
# first = 5
# # 여기에 코드 작성


# first = 5
# # 여기에 코드 작성
# while first >= 1:
#     if first == 2:
#         print("special")
    
#     # 현재 first 값 출력 (선택 사항)
#     print(first) 
    
#     first = first - 1 # first 값을 1씩 감소

# 

# ✅ 중급 난이도 문제 3 — 리스트 합계 및 평균 계산
# kor와 eng 리스트가 주어졌을 때,
# 각 학생 점수의 총합을 total_scores 리스트로 저장


# 각 학생 점수 평균을 avg_scores 리스트로 저장


# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]

# # 여기에 코드 작성
# # 출력 예시:
# # total_scores = [160, 160, 160, 110, 110]
# # avg_scores = [80.0, 80.0, 80.0, 55.0, 55.0]


kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

# 여기에 코드 작성
total_scores = []
avg_scores = []

# zip()을 사용하여 kor와 eng 리스트의 요소를 짝지어 순회
# for k, e in zip(kor, eng):
#     # 총점 계산
#     total = k + e
#     total_scores.append(total)
    
#     # 평균 계산 (2과목이므로 2로 나누고, 소수점 출력을 위해 2.0으로 나눔)
#     average = total / 2.0 
#     avg_scores.append(average)

# print(f"total_scores = {total_scores}")
# print(f"avg_scores = {avg_scores}")

# ✅ 중급 난이도 문제 4 — 누적 합과 조건문 결합
# kor 리스트에서 60점 이상인 점수만 누적 합계를 계산하고 출력하시오.
# 조건: for문 사용, 60점 미만은 제외


# kor = [70, 80, 90, 40, 50]

# # 여기에 코드 작성
# # 출력 예시: 누적합 = 240

# kor = [70, 80, 90, 40, 50]

# # 여기에 코드 작성
# total_sum = 0 # 누적 합계를 저장할 변수 초기화

# for score in kor:
#     # 점수가 60점 이상인지 확인
#     if score >= 60:
#         # 60점 이상일 경우에만 누적 합계에 더함
#         total_sum += score

# print(f"누적합 = {total_sum}")