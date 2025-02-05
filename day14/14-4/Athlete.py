class Athlete:
    def __init__(self, name, sport, record):
        self.name = name      # 선수 이름
        self.sport = sport    # 종목
        self.record = record  # 기록 (예: 시간, 점수 등)
    
    def update_record(self, new_record):
        """기록 업데이트"""
        self.record = new_record
        print(f"{self.name}의 기록이 {new_record}로 업데이트되었습니다.")
    
    def display_info(self):
        """선수 정보 출력"""
        print(f"이름: {self.name}")
        print(f"종목: {self.sport}")
        print(f"기록: {self.record}")


if __name__ == '__main__':
    athlete = Athlete("홍길동", "100m 달리기", "10.5초")
    athlete.display_info()
    athlete.update_record("10.3초")
    athlete.display_info()