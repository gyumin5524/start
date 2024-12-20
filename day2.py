#1.사용자의 이름을 입력받아 "안녕하세요, [이름]님!"이라고 출력하는 함수say_hello를 작성하세요.
# def say_hello(name="[이름]"):
#     print(f"안녕하세요,{name}님!")

# say_hello()
# #say_hello("봉현튜텨님")


#2.두 개의 숫자를 입력받아 큰 수를 반환하는 함수 find_larger를 작성하세요.
# def find_larger(n1,n2):
#         return n1 if n1 > n2 else n2
# result = find_larger(10, 20)
# print(f"더 큰 수는: {result}")

# def find_larger():
#     n1, n2 = map(int,input().split())
#     return n1 if n1 > n2 else n2

# result = find_larger()
# print(f"더 큰 수는: {result}")

# def print_first_last():
#     fnum = int(input("첫번째 수를 입력하세요."))
#     snum = int(input("두번째 수를 입력하세요."))
#     if fnum > snum :
#         print(f"입력한 두 수 중 큰 수는 {fnum}입니다")
#     else :
#         print(f"입력한 두 수 중 큰 수는 {snum}입니다")

# print_first_last()


#3.리스트를 입력받아 그 리스트의 첫 번째 요소와 마지막 요소를 출력하는 함수 print_first_last를 작성하세요.
# def print_first_last(lst):
#     return lst[0], lst[-1]

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(print_first_last(lst))

#4.숫자를 하나 입력받아 그 숫자가 짝수인지 홀수인지 출력하는 함수 even_or_odd를 작성하세요.
# def even_or_odd():
#     num = int(input("숫자를 입력해주세요."))
#     if num % 2 == 0 :
#         print(num, "은 짝수입다.")
#     else :
#         print(num, "은 홀수입니다.")

# even_or_odd()

#5.문자열을 입력받아 그 문자열을 대문자로 변환하여 반환하는 함수 to_uppercase를 작성하세요.
# def to_uppercase():
#     name = input("문자만 입력해주세요.")
#     return print(name.upper())

# to_uppercase()

#int(input(f"문자를 입력해주세요."))

#6.두 숫자를 입력받아 더한 결과를 반환하는 함수 add_numbers를 작성하세요.
# def add_numbers(n1, n2):
#     return n1 + n2

# print(add_numbers(n1, n2))  #원하는 숫자 입력 n1,n2

# def add_numbers():
#     n1 = int(input("첫 번째 숫자 입력"))
#     n2 = int(input("두 번째 숫자 입력"))
#     result = n1 + n2
#     return print(f"두 숫자의 합은 {result}")
# add_numbers()

# def add_numbers():
#     n1, n2 = map(int,input("숫자 두개 입력").split())
#     result = n1 + n2
#     print(f"두 숫자의 합은 {result}")
#     return result
# add_numbers()
    
#7.리스트를 입력받아 모든 요소의 합을 반환하는 함수 sum_list를 작성하세요. (내장 함수 sum을 사용하지 않고 구현해보세요.)
# def sum_list(list):
#     total = 0
#     for number in list:
#         total += number
#     return total
# list = [2,4,6]
# list2 = [1,3,5]

# print(sum_list(list))
# print(sum_list(list2))
# sum_list(list)

#8.임의의 개수의 숫자를 입력받아 그 평균을 계산하는 함수 calculate_average를 작성하세요. (가변 인자를 사용하세요.)
# def calculate_average(*numbers):
#     if not numbers:                 # numbers가 비어있는 경우를 처리
#         return 0    
#     return sum(numbers) / len(numbers)

# print(calculate_average(1,2,3,4,5,6,7,8,9,10))
# print(calculate_average(5,15))
# print(calculate_average())


#9.문자열을 입력받아 그 문자열의 길이를 반환하는 람다 함수를 작성하세요.
# def len_lambda():
#     str_len = lambda s : len(s)
#     return print(str_len("hello world"))

# len_lambda()


# #input을 사용해서 검색한 문자의 길이를 보게하는 코드
# def len_lambda():
#     str_len = lambda s : len(s)
#     search = input("문자를 입력하세요:")
#     print(f"입력한 문자열의 길이는{str_len(search)}입니다.")

# len_lambda()


#10.딕셔너리를 입력받아 키와 값을 바꾼 새로운 딕셔너리를 반환하는 함수 swap_dict를 작성하세요.
# def swap_dict(input_dict):
#     return {v:k for k, v in input_dict.items()}
# list_dict = {"a":1, "b":2, "c":3}
# swap_dict = swap_dict(list_dict)

# print(list_dict)    #원래 딕셔너리
# print(swap_dict)    #키와 값을 바꾼 딕셔너리


#11.기본 매개변수를 사용하여 인사말을 출력하는 함수 greet를 작성하세요. 이름이 주어지지 않으면 "Guest"라고 인사하도록 합니다.
# def greet():
#     name="Guest"
#     print(f"안녕하세요,{name}님!")

# greet()