# 공통 사항 : 제출 문제마다 function 실행은 최소 3회 호출

# 🔹 문제 1
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.

def avg_celsius(t1, t2, t3):
    
    average = (t1 + t2 + t3) / 3
    return average

# 함수 호출 (최소 3회)
print(f"평균 온도 1: {avg_celsius(20, 25, 30)}도")
print(f"평균 온도 2: {avg_celsius(15, 18, 21)}도")
print(f"평균 온도 3: {avg_celsius(10, 10, 10)}도")
print(f"평균 온도 4: {avg_celsius(0, 5, -5)}도")


# 🔹 문제 2
# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.
def print_favorite_languages(name, lang1, lang2):
  
    print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")

# 함수 호출 (최소 3회)
print_favorite_languages("홍길동", "Python", "Java")
print_favorite_languages("김철수", "JavaScript", "TypeScript")
print_favorite_languages("이영희", "C++", "Go")
print_favorite_languages("박민수", "Rust", "Kotlin")

# 🔹 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.
def sum_pass_scores(scores):
   
    total = 0
    for score in scores:
        if score >= 60:
            total += score
    return total

# 함수 호출 (최소 3회)
scores1 = [85, 90, 55, 70, 45]
scores2 = [100, 95, 88, 92]
scores3 = [30, 40, 50, 55]
scores4 = [60, 60, 60]

print(f"합격 점수 합계 1: {sum_pass_scores(scores1)}점")
print(f"합격 점수 합계 2: {sum_pass_scores(scores2)}점")
print(f"합격 점수 합계 3: {sum_pass_scores(scores3)}점")
print(f"합격 점수 합계 4: {sum_pass_scores(scores4)}점")

# 🔹 문제 4
# 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.
def combine(str1, str2):
    
    return str1 + str2

# 함수 호출 (최소 3회)
result1 = combine("안녕하세요, ", "파이썬입니다!")
result2 = combine("Hello ", "World!")
result3 = combine("Python은 ", "재미있습니다.")
result4 = combine("오늘 날씨는 ", "맑습니다.")

print(result1)
print(result2)
print(result3)
print(result4)
# 🔹 문제 5
# 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.

def fahrenheit_to_celsius_list(temps):
   
    celsius_list = []
    for temp in temps:
        celsius = (temp - 32) * 5 / 9
        celsius_list.append(celsius)
    return celsius_list

# 함수 호출 (최소 3회)
fahrenheit1 = [32, 77, 95, 212]
fahrenheit2 = [0, 50, 100]
fahrenheit3 = [68, 86, 104]
fahrenheit4 = [-40, 32, 212]

print(f"섭씨 온도 1: {fahrenheit_to_celsius_list(fahrenheit1)}")
print(f"섭씨 온도 2: {fahrenheit_to_celsius_list(fahrenheit2)}")
print(f"섭씨 온도 3: {fahrenheit_to_celsius_list(fahrenheit3)}")
print(f"섭씨 온도 4: {fahrenheit_to_celsius_list(fahrenheit4)}")

