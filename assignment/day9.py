# 1. 사용자로부터 숫자를 입력받아 짝수인지 홀수인지 판별하는 프로그램을 작성하세요.
# def check_even_odd(number):
#     if number % 2 == 0:
#         return "짝수입니다."
#     else:
#         return "홀수입니다."

# print(check_even_odd(int(input("숫자를 입력하세요: "))))


# 2. 1부터 100까지의 숫자 중 3의 배수만 출력하는 프로그램을 작성하세요.
# def print_multiples_of_3():
#     return [i for i in range(1, 101) if i % 3 == 0]

# print(print_multiples_of_3())


# 3. 사용자로부터 점수를 입력받아 A, B, C, D, F 등급을 출력하는 프로그램을 작성하세요. (90이상 A, 80이상 B, 70이상 C, 60이상 D, 60미만 F)
# def grade(score):
#     if score >= 90:
#         return "A등급"
#     elif score >= 80:
#         return "B등급"
#     elif score >= 70:
#         return "C등급"
#     elif score >= 60:
#         return "D등급"
#     else:
#         return "F등급"

# print(grade(int(input("점수를 입력하세요: "))))


# 4. 구구단 7단을 출력하는 프로그램을 작성하세요.
# def print_gugudan_7():
#     return [f"7 x {i} = {7 * i}" for i in range(1, 10)]

# print(print_gugudan_7())


# 5. 1부터 100까지의 숫자 중 3의 배수이면서 5의 배수인 숫자를 모두 출력하는 프로그램을 작성하세요.
# def multiples_of_3_and_5():
#     return [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]

# print(multiples_of_3_and_5())


# 6. 사용자로부터 숫자를 입력받아 그 숫자의 팩토리얼을 계산하는 프로그램을 작성하세요.
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(int(input("팩토리얼 계산할 숫자를 입력하세요: "))))


# 7. 1부터 100까지의 숫자 중 소수(prime number)만 출력하는 프로그램을 작성하세요.
# def prime_numbers():
#     primes = []
#     for num in range(2, 101):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes

# print(prime_numbers())


# 8. 사용자로부터 숫자 n을 입력받아 피보나치 수열의 n번째 항까지 출력하는 프로그램을 작성하세요.
# def fibonacci(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence

# print(fibonacci(int(input("피보나치 수열의 항 수를 입력하세요: "))))


# 9. 사용자로부터 문자열을 입력받아 그 문자열이 팰린드롬(앞뒤로 읽어도 같은 문자열)인지 판별하는 프로그램을 작성하세요.
# def is_palindrome(string):
#     return string == string[::-1]

# print("팰린드롬 여부:", is_palindrome(input("문자열을 입력하세요: ")))


# 10. 1부터 100까지의 숫자를 출력하되, 3의 배수는 "Fizz", 5의 배수는 "Buzz", 3과 5의 공배수는 "FizzBuzz"를 출력하는 프로그램을 작성하세요.
# def fizz_buzz():
#     result = []
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
#     return result

# print(fizz_buzz())