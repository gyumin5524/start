# 1. 사용자로부터 이름을 입력받아 "안녕하세요, [이름]님!"을 출력하는 프로그램을 작성하세요.
# def greet_user():
#     name = input("이름을 입력하세요: ")
#     print(f"안녕하세요, {name}님!")

# greet_user()


# 2. 1부터 10까지의 숫자를 출력하는 프로그램을 작성하세요.
# def print_numbers_1_to_10():
#     print("1부터 10까지의 숫자:")
#     for i in range(1, 11):
#         print(i, end=" ")
#     print()

# print_numbers_1_to_10()


# 3. 사용자로부터 숫자를 입력받아 양수인지 음수인지 또는 0인지 판별하는 프로그램을 작성하세요.
# def check_number():
#     num = int(input("숫자를 입력하세요: "))
#     if num > 0:
#         print("양수입니다.")
#     elif num < 0:
#         print("음수입니다.")
#     else:
#         print("0입니다.")

# check_number()


# 4. 1부터 20까지의 짝수만 출력하는 프로그램을 작성하세요.
# def print_even_numbers_1_to_20():
#     print("1부터 20까지의 짝수:")
#     for i in range(1, 21):
#         if i % 2 == 0:
#             print(i, end=" ")
#     print()

# print_even_numbers_1_to_20()


# 5. 사용자로부터 5개의 숫자를 입력받아 그 합계를 출력하는 프로그램을 작성하세요.
# def sum_of_5_numbers():
#     numbers = []
#     print("숫자 5개를 입력하세요:")
#     for _ in range(5):
#         numbers.append(int(input()))
#     print(f"입력한 숫자의 합계: {sum(numbers)}")

# sum_of_5_numbers()


# 6. 구구단 2단을 출력하는 프로그램을 작성하세요.
# def print_gugudan_2():
#     print("구구단 2단:")
#     for i in range(1, 10):
#         print(f"2 x {i} = {2 * i}")
# print_gugudan_2()


# 7. 사용자로부터 숫자를 입력받아 1부터 그 숫자까지의 합을 계산하는 프로그램을 작성하세요.
# def sum_up_to_n():
#     n = int(input("숫자를 입력하세요: "))
#     total = sum(range(1, n + 1))
#     print(f"1부터 {n}까지의 합: {total}")

# sum_up_to_n()


# 8. 1부터 10까지의 숫자 중 3의 배수만 출력하는 프로그램을 작성하세요.
# def print_multiples_of_3_up_to_10():
#     print("1부터 10까지의 숫자 중 3의 배수:")
#     for i in range(1, 11):
#         if i % 3 == 0:
#             print(i, end=" ")
#     print()

# print_multiples_of_3_up_to_10()


# 9. 사용자로부터 숫자를 입력받아 그 숫자의 절대값을 출력하는 프로그램을 작성하세요.
# def print_absolute_value():
#     num = int(input("숫자를 입력하세요: "))
#     print(f"{num}의 절대값: {abs(num)}")

# print_absolute_value()


# 10. 사용자로부터 세 개의 숫자를 입력받아 가장 큰 수를 출력하는 프로그램을 작성하세요.
# def find_largest_of_three():
#     nums = []
#     print("숫자 3개를 입력하세요:")
#     for _ in range(3):
#         nums.append(int(input()))
#     print(f"가장 큰 수: {max(nums)}")

# find_largest_of_three()