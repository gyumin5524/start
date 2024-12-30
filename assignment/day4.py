# 1. "Book" 클래스를 만드세요.
#     - 인스턴스 변수: title, author, price
#     - 인스턴스 메서드: get_info() (책 정보 반환)

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def get_info(self):
#         return f"제목: {self.title}, 저자: {self.author}, 가격: {self.price}"

# book1 = Book("과제어려워", "조규민", 100)

# print(book1.get_info())


# 2. "BankAccount" 클래스를 만드세요.
#     - 인스턴스 변수: account_number, balance
#     - 인스턴스 메서드: deposit(amount), withdraw(amount)

# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount}를 입금했습니다. 현재 잔액: {self.balance}원" )

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"{amount}를 출금했습니다. 현재 잔액: {self.balance}원")
#         else:
#             print("잔액이 부족합니다.")

# account = BankAccount("123-45-123", 30000)

# print(f"account_nunmber: {account.account_number} ")
# print(f"balance: {account.balance} ")

# account.deposit(10000)
# account.withdraw(5000)
# account.withdraw(20000)


# 3. "Student" 클래스를 만드세요.
#     - 인스턴스 변수: name, grade, scores (과목별 점수 딕셔너리)
#     - 인스턴스 메서드: add_score(subject, score), get_average()
#     - 클래스 변수: school_name
#     - 클래스 메서드: change_school_name(new_name)

# class Student:
#     school_name = "학교"

#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#         self.scores = {}

#     def add_score(self, subject, score):
#         self.scores[subject] = score

#     def get_average(self):
#         if not self.scores:
#             return "아직 성적이 없습니다."
#         return sum(self.scores.values()) / len(self.scores)

#     @classmethod
#     def change_school_name(cls, new_name):
#         cls.school_name = new_name

# student1 = Student("조규민", 3)

# student1.add_score("수학", 20)
# student1.add_score("영어", 30)
# student1.add_score("과학", 40)

# print(student1.name, "의 평균 점수:", student1.get_average())

# Student.change_school_name("스파르타학교")
# print("학교 이름:", Student.school_name)


# 4. "Product" 클래스를 만드세요.
#     - 인스턴스 변수: name, price, stock
#     - 인스턴스 메서드: sell(quantity), restock(quantity)
#     - 클래스 변수: total_products
#     - 클래스 메서드: get_total_products()
#     - 정적 메서드: is_in_stock(stock) (재고가 1개 이상이면 True 반환)

# class Product:
#     total_products = 0

#     def __init__(self, name, price, stock=0):
#         self.name = name
#         self.price = price
#         self.stock = stock
#         Product.total_products += 1

#     def sell(self, quantity):
#         if self.stock >= quantity:
#             self.stock -= quantity
#             print(f"{self.name} 제품 {quantity}개 판매 완료. 남은 재고: {self.stock}개")
#         else:
#             print("재고가 부족합니다.")

#     def restock(self, quantity):
#         self.stock += quantity
#         print(f"{self.name} 제품 {quantity}개 입고 완료. 현재 재고: {self.stock}개")

#     @classmethod
#     def get_total_products(cls):
#         return cls.total_products

#     @staticmethod
#     def is_in_stock(stock):
#         return stock > 0

# product1 = Product("스마트폰", 1000000, 100)
# product2 = Product("노트북", 2000000, 100)

# product1.sell(10)
# product2.restock(10)

# print(f"총 제품 수: {Product.get_total_products()}개")
# print(f"재고가 있는지 확인: {Product.is_in_stock(product1.stock)}")


# 5. "Car" 클래스를 만드세요.
#     - 인스턴스 변수: make, model, year
#     - 인스턴스 메서드: get_info()
#     - 클래스 변수: total_cars
#     - 클래스 메서드: get_total_cars()
#     - 정적 메서드: is_antique(year) (25년 이상된 차면 True 반환)

# class Car:
#     total_cars = 0

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         Car.total_cars += 1

#     def get_info(self):
#         return f"제조사: {self.make}, 모델: {self.model}, 연식: {self.year}"

#     @classmethod
#     def get_total_cars(cls):
#         return cls.total_cars

#     @staticmethod
#     def is_antique(year):
#         return year <= 2023 - 25

# car1 = Car("현대", "쏘나타", 2020)
# car2 = Car("기아", "K5", 1998)
# car3 = Car("현대", "쏘나타", 2023)
# car4 = Car("기아", "K5", 2005)

# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())
# print(car4.get_info())

# print(f"총 자동차 수: {Car.get_total_cars()}대")

# print(f"car1는 클래식카입니까? {Car.is_antique(car1.year)}")
# print(f"car2는 클래식카입니까? {Car.is_antique(car2.year)}")
# print(f"car3는 클래식카자동차입니까? {Car.is_antique(car3.year)}")
# print(f"car4는 클래식카입니까? {Car.is_antique(car4.year)}")