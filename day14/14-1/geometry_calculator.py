from math_operations import circle_area, circle_circumference

def main():
    try:
        radius = float(input("원의 반지름을 입력하세요: "))
        area = circle_area(radius)
        circumference = circle_circumference(radius)
        print(f"원의 면적: {area:.2f}")
        print(f"원의 둘레: {circumference:.2f}")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

if __name__ == '__main__':
    main()