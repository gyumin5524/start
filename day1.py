#1.주어진 문자열에서 각 문자의 출현 빈도를 계산하는 딕셔너리 컴프리헨션을 작성하세요.
def freq_dict():
    text = "Frequency of bleeding in characters"
    frequency = {str: text.count(str) for str in set(text)}
    print(frequency)

#freq_dict()
# 딕셔너리 안에 set을 넣었을 때와 그냥 딕셔너리 성질로 중복값 제거를 했을 때 시간복잡도에 차이가 있는가?

#2.1부터 100까지의 숫자 중 3의 배수이면서 5의 배수인 숫자만을 포함하는 리스트를 리스트 컴프리헨션으로 생성하세요.
def numbers_list():
    numbers = [x for x in range(1,101) if x % 3 == 0 and x % 5 ==0]
    print(numbers)

#numbers_list()


#3.두 개의 리스트가 주어졌을 때, 이를 딕셔너리로 결합하는 딕셔너리 컴프리헨션을 작성하세요.
def list2_dict():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    list2_dict = {k: v for k, v in zip(keys, values)}
    print(list2_dict)

#list2_dict()


#4.주어진 리스트에서 중복을 제거하고 고유한 요소만을 포함하는 새로운 리스트를 생성하세요. (힌트: set 사용)
def list_set():
    original_list = [1, 2, 2, 3, 4, 4, 5]
    duplication = list(set(original_list))
    print(duplication)

#list_set()
    
    
#5.2차원 리스트를 생성하는 리스트 컴프리헨션을 작성하세요. (예: 5x5 행렬)
def matrix_list():
    matrix = [[i for j in range(5)] for i in range(5)]
    print(matrix)

#matrix_list()
    
    
#6.주어진 문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 변환하여 새로운 리스트를 만드세요.
def str_list():
    string_list = ['apple', 'banana', 'pear', 'grape', 'kiwi']
    new_list = [str_l.upper() for str_l in string_list if len(str_l) >= 5]
    print(new_list)

#str_list()


#7.두 개의 집합 A와 B가 주어졌을 때, 두 집합의 대칭 차집합을 구하세요.
def symmetry_set():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    sym_diff = (set_a - set_b) | (set_b - set_a)  #sym_diff = set_a ^ set_b 하면됨...
    #sym_diff = list(set(set_a)^ set(set_b))
    #sym_diff = list(set(set_a).symmetric_difference(set_b))
    print(sym_diff)

#symmetry_set()
    

#8.1부터 10까지의 숫자에 대해 각 숫자의 제곱을 값으로 갖는 딕셔너리를 생성하세요.
def square_dict():
    squr = {s: s**2 for s in range(1, 11)}
    print(squr)

#square_dict()

#9.주어진 리스트에서 짝수만 선택하여 그 제곱값을 가진 새로운 리스트를 생성하세요.
def new_list():
    given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squr = [s**2 for s in given_list if s % 2 == 0]
    print(squr)

#new_list()

#10.여러 개의 리스트가 주어졌을 때, 이들을 하나의 리스트로 평탄화하는 함수를 작성하세요.  
def flat_list():
    lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flat = [n for m in lists for n in m]
    print(flat)
    
#flat_list()

class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

obj = Child()
print(obj.greet())