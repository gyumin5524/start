# 1. "Animal", "Flyable", "Swimmable" 클래스를 만들고, 이를 다중상속받는 "Duck" 클래스를 만드세요.
#     - Animal: name 인스턴스 변수, speak() 메서드
#     - Flyable: fly() 메서드
#     - Swimmable: swim() 메서드

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return f"{self.name}가 소리를 냅니다"

# class Flyable:
#     def fly(self):
#         return "날 수 있어요"

# class Swimmable:
#     def swim(self):
#         return "수영할 수 있어요"

# class Duck(Animal, Flyable, Swimmable):
#     def __init__(self, name):
#         super().__init__(name)

# duck = Duck("오리")
# print(duck.speak())
# print(duck.fly())
# print(duck.swim())


# 2. "Person" 클래스와 이를 상속받는 "Student" 클래스를 만드세요.
#     - Person: name, age 인스턴스 변수, init, introduce() 메서드
#     - Student: grade 인스턴스 변수 추가, introduce() 메서드 오버라이드
#     - Student에 lt 매직 메서드 추가 (grade 기준 비교)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         return f"안녕하세요, 저는 {self.name}이고 {self.age}입니다"

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age) #부모 클래스 Person의 __init__ 호출
#         self.grade = grade

#     def introduce(self):
#         return f"안녕하세요, 저는 {self.name}이고 {self.age}살이며 {self.grade}학년입니다"
    
#     def __lt__(self, other):
#         return self.grade < other.grade

# student1 = Student("학생1", 20, 1)
# student2 = Student("학생2", 21, 2)

# print(student1.introduce())
# print(student2.introduce())
# print(student1 < student2)


# 3. "Shape" 추상 클래스와 이를 상속받는 "Circle"과 "Rectangle" 클래스를 만드세요.
#     - Shape: 추상 메서드 area(), perimeter()
#     - Circle, Rectangle: Shape 메서드 구현
#     - Circle에 radius 프로퍼티 추가 (음수 방지)

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self._radius = radius
    
#     @property
#     def radius(self):
#         return self._radius
    
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError("반지름은 음수가 될 수 없다")
#         self._radius = value

#     def area(self):
#         return 3.14 * self._radius ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self._radius

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)

# circle = Circle(5)
# print(circle.area())
# print(circle.perimeter())

# rectangle = Rectangle(4, 5)
# print(rectangle.area())
# print(rectangle.perimeter())



#  4. "Playlist" 클래스를 만들고 이에 대한 매직 메서드를 구현하세요.
#      - init, len, getitem, setitem, iter 구현
#      - songs 리스트를 관리하는 클래스로 만들기

# class Playlist:
#     def __init__(self):
#         self.songs = []
    
#     def __len__(self):
#         return len(self.songs)
    
#     def __getitem__(self, index):
#         return self.songs[index]
    
#     def __setitem__(self, index, value):
#         self.songs[index] = value
    
#     def __iter__(self):
#         return iter(self.songs)
    
#     def add_song(self, song):
#         self.songs.append(song)

# playlist = Playlist()
# playlist.add_song("Song 1")
# playlist.add_song("Song 2")

# print(len(playlist))
# print(playlist[0])

# playlist[1] = "New Song 2"
# for song in playlist:
#     print(song)


#  5. "Temperature" 클래스를 만들고 섭씨/화씨 변환을 위한 프로퍼티를 구현하세요.
#      - celsius 프로퍼티: 섭씨 온도 설정/반환
#      - fahrenheit 프로퍼티: 화씨 온도 설정/반환
#      - eq, lt 매직 메서드 추가 (섭씨 온도 기준 비교)

# class Temperature:
#     def __init__(self, celsius=0):
#         self._celsius = celsius
    
#     @property
#     def celsius(self):
#         return self._celsius
    
#     @celsius.setter
#     def celsius(self, value):
#         self._celsius = value
    
#     @property
#     def fahrenheit(self):
#         return self._celsius * 9 / 5 + 32
    
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self._celsius = (value - 32) * 5 / 9
    
#     def __eq__(self, other):
#         return self.celsius == other.celsius
    
#     def __lt__(self, other):
#         return self.celsius < other.celsius

# temp1 = Temperature(0)
# temp2 = Temperature(100)

# print(temp1.fahrenheit)
# temp1.fahrenheit = 212
# print(temp1.celsius)
# print(temp1 == temp2)
# print(temp1 < temp2)
