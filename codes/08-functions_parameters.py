#함수 사용

# def function_name(praram_first,...param_last):
#     # 실행할 코드
#     return return_value

# 점수 총합 함수 작성 
kor = 60
eng = 70
math = 80

# sum = kor + eng 

def get_sum(korean, english,mathatics):
    # 실행할 코드

    summation = korean + english + mathatics
    return summation

# sum = get_sum(kor, eng ,0)
# print(f"총점: {sum}")

# sum = get_sum(kor, eng, math)
# print(f"총점: {sum}")

#for ans gkatn wkrtjd
# kor_scores = [90,80,70,60,50]
# eng_scores = [80,70,60,50,40]
# math_scores = [70,60,50,40,30]  

# length = len(kor_scores)
# len_list = range(length)

# range(len(kor_scores))
# pass

def get_sum(korean, english, math):
    return korean + english + math

korean_scores = [90, 85, 88]
english_scores = [80, 92, 78]
math_scores = [95, 88, 90]

def get_for_sum(korean_scores, english_scores, math_scores):
    for i in range(len(korean_scores)):
        total = get_sum(korean_scores[i], english_scores[i], math_scores[i])
        print(f"{i+1}번째 학생 총점: {total}")

get_for_sum(korean_scores, english_scores, math_scores)
