def main():
    try:
        # 1. 사용자 입력 받기
        raw = input()                          # 예: "3 1 4 2"
        parts = raw.split()                    # 예: ["3", "1", "4", "2"]
        numbers = [float(p) for p in parts]    # 예: [3.0, 1.0, 4.0, 2.0]

        if not numbers:
            raise ValueError

        # 2. 직접 정렬 (선택 정렬)
        n = len(numbers)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            # 자리 바꾸기
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

        # 3. 출력
        result = " ".join(str(num) for num in numbers)
        print(f"Sorted: {result}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
