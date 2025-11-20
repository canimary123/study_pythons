{
  "task_info": {
    "title": "사칙연산 함수 구현",
    "target_file_path": "prompts/01_functions.py",
    "language": "python"
  },
  "prompt_content": {
    "goal": "두 개의 숫자 리스트를 이용해 사칙연산(+, -, *, /)을 수행하는 함수를 구현하시오.",
    "requirements": [
      "테스트 데이터는 반드시 리스트(list) 형태로 제공할 것",
      "테스트 데이터의 개수는 총 10개로 맞출 것",
      "변수명 명명 규칙은 스네이크 케이스(소문자 + _)를 따를 것",
      "함수는 두 개의 숫자를 인자로 받아 덧셈, 뺄셈, 곱셈, 나눗셈의 결과를 모두 반환할 것",
      "나눗셈 수행 시 분모가 0인 경우, 결과값으로 'division_error' 문자열을 반환할 것"
    ],
    "code_skeleton": [
      "# 테스트 리스트 (10개)",
      "test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]",
      "test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]",
      "",
      "def calculate_operations(a, b):",
      "    # 여기에 코드를 작성하세요",
      "    pass",
      "",
      "# 테스트 실행",
      "for i in range(10):",
      "    a = test_a[i]",
      "    b = test_b[i]",
      "    result = calculate_operations(a, b)",
      "    print(f\"{a}, {b} => {result}\")"
    ]
  }
}