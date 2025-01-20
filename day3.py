#1. 람다 함수를 사용하여 주어진 리스트의 모든 요소를 제곱하는 함수를 작성하세요.
# def square_labda(lst):
#     return [(lambda x: x**2)(x) for x in lst]

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = square_labda(numbers)
# print(squared_numbers)


#2. map() 함수와 람다 함수를 사용하여 문자열 리스트의 각 단어의 길이를 구하는 코드를 작성하세요.
# def word_lengths(words):
#     return list(map(lambda word: len(word), words))

# word_list = ["apple", "banana", "cherry", "pineapple"]
# lengths = word_lengths(word_list)
# print(lengths)  


#3. filter() 함수를 사용하여 1부터 20까지의 숫자 중 짝수만 선택하는 코드를 작성하세요.
# def is_even(x):
#     return x % 2 == 0

# even_numbers = list(filter(is_even, range(1, 21)))
# print(even_numbers)


#4. reduce() 함수를 사용하여 리스트의 모든 요소를 곱하는 함수를 작성하세요.
# from functools import reduce

# def multiply_elements(lst):
#     return reduce(lambda x, y: x * y, lst)

# numbers = [1, 2, 3, 4, 5]
# result = multiply_elements(numbers)
# print(result)


# 0! = 1 
# 1! = 1
#5. 재귀 함수를 사용하여 팩토리얼(n!)을 계산하는 함수 **`factorial`**을 작성하세요.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# result = factorial(5) #()에 숫자입력하기
# print(result)


#해설이 필요합니다... 너무 어렵습니다...
# 6. 데코레이터를 만들어 함수의 실행 시간을 측정하는 코드를 작성하세요. 
# import time
# from functools import wraps

# def timing_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # 시작 시간 기록
#         result = func(*args, **kwargs)  # 원래 함수 실행
#         end_time = time.time()  # 종료 시간 기록
#         execution_time = end_time - start_time  # 실행 시간 계산
#         print(f"함수 '{func.__name__}'의 실행 시간: {execution_time:.2f}초")
#         return result
#     return wrapper

# # 데코레이터를 사용한 예시 함수
# @timing_decorator
# def example_function(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total

# # 함수 호출
# result = example_function(1000000)
# print(f"결과: {result}")


#7. 'Person' 클래스를 정의하고, 이름과 나이를 속성으로 가지며, 자기 소개를 하는 메서드를 포함하세요.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce_myself(self):
#         print(f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다.")


# person = Person("조규민", 31)
# person.introduce_myself()