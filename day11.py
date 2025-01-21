# 1. 사용자로부터 숫자를 입력받아 해당 숫자가 양수, 음수, 또는 0인지 판별하는 프로그램을 작성하세요.
# def check_number():
#     num = int(input("숫자를 입력하세요: "))
#     if num > 0:
#         print("양수입니다.")
#     elif num < 0:
#         print("음수입니다.")
#     else:
#         print("0입니다.")

# check_number()


# 2. 1부터 100까지의 숫자 중 7의 배수만 출력하는 프로그램을 작성하세요.
# def multiples_of_7():
#     print("1부터 100까지의 7의 배수:")
#     for i in range(1, 101):
#         if i % 7 == 0:
#             print(i, end=" ")
#     print()

# multiples_of_7()


# 3. 사용자로부터 두 개의 숫자를 입력받아 두 숫자 사이의 모든 정수를 출력하는 프로그램을 작성하세요.
# def print_numbers_between():
#     start = int(input("첫 번째 숫자를 입력하세요: "))
#     end = int(input("두 번째 숫자를 입력하세요: "))
#     print(f"{start}부터 {end}까지의 숫자:")
#     for i in range(start, end + 1):
#         print(i, end=" ")
#     print()

# print_numbers_between()


# 4. 1부터 10까지의 숫자에 대해 각 숫자의 제곱을 출력하는 프로그램을 작성하세요.
# def print_squares():
#     print("1부터 10까지의 숫자와 그 제곱:")
#     for i in range(1, 11):
#         print(f"{i}^2 = {i ** 2}")

# print_squares()


# 5. 사용자로부터 문자열을 입력받아 각 문자를 한 줄에 하나씩 출력하는 프로그램을 작성하세요.
# def print_characters():
#     text = input("문자열을 입력하세요: ")
#     print("입력한 문자열의 각 문자:")
#     for char in text:
#         print(char)

# print_characters()


# 6. 1부터 100까지의 숫자 중 3의 배수이거나 5의 배수인 숫자의 합을 계산하는 프로그램을 작성하세요.
# def sum_of_multiples():
#     total = sum(i for i in range(1, 101) if i % 3 == 0 or i % 5 == 0)
#     print(f"1부터 100까지 3의 배수 또는 5의 배수의 합: {total}")

# sum_of_multiples()


# 7. 사용자로부터 숫자 n을 입력받아 1부터 n까지의 팩토리얼을 계산하는 프로그램을 작성하세요.
# def calculate_factorial():
#     n = int(input("팩토리얼을 계산할 숫자를 입력하세요: "))
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     print(f"{n}! = {factorial}")

# calculate_factorial()


# 8. 구구단 2단부터 9단까지를 출력하는 프로그램을 작성하세요.
# def print_multiplication_tables():
#     print("구구단 2단부터 9단:")
#     for i in range(2, 10):
#         for j in range(1, 10):
#             print(f"{i} x {j} = {i * j}")
#         print()

# print_multiplication_tables()


# 9. 사용자로부터 숫자를 계속 입력받다가 0을 입력하면 입력을 중단하고, 입력받은 숫자들의 평균을 출력하는 프로그램을 작성하세요.
# def calculate_average():
#     numbers = []
#     while True:
#         num = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))
#         if num == 0:
#             break
#         numbers.append(num)
#     if numbers:
#         avg = sum(numbers) / len(numbers)
#         print(f"입력한 숫자의 평균: {avg}")
#     else:
#         print("입력된 숫자가 없습니다.")

# calculate_average()


# 10. 다음과 같은 패턴을 출력하는 프로그램을 작성하세요.
def print_pattern():
    print("패턴 출력:")
    for i in range(1, 6):
        print("*" * i)

print_pattern()
