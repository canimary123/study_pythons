# 01_functions.py

# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

def calculate_operations(a, b):
    # """
    # 두 숫자를 입력받아 사칙연산 결과를 반환하는 함수
    # 나눗셈 시 분모가 0이면 'division_error' 반환
    # """
    add_result = a + b
    sub_result = a - b
    mul_result = a * b
    
    # 0으로 나누기 예외 처리
    if b == 0:
        div_result = "division_error"
    else:
        div_result = a / b
        
    return add_result, sub_result, mul_result, div_result

# 테스트 실행
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    result = calculate_operations(a, b)
    print(f"{a}, {b} => {result}")