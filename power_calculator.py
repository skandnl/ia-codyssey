def main():
    """사용자로부터 숫자와 지수를 입력받아 거듭제곱을 계산하고 출력합니다."""
    try:
        # 사용자로부터 밑(base) 입력받기
        base_input = input("Enter number: ")
        base = float(base_input)

    except ValueError:
        print("Invalid number input.")
        return # 숫자 형식이 아니면 함수 종료

    try:
        # 사용자로부터 지수(exponent) 입력받기
        exponent_input = input("Enter exponent: ")
        exponent = int(exponent_input)

    except ValueError:
        print("Invalid exponent input.")
        return # 정수 형식이 아니면 함수 종료

    # 거듭제곱 계산 (반복문 사용)
    result = 1.0
    for _ in range(exponent):
        result *= base

    print(f"Result: {result}")


# 이 스크립트가 직접 실행될 때 main 함수를 호출
if __name__ == "__main__":
    main()