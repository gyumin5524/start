class Recipe:
    def __init__(self, name, ingredients, cooking_time):
        """
        :param name: 레시피 이름 (문자열)
        :param ingredients: 필요한 재료 목록 (리스트)
        :param cooking_time: 조리 시간 (분 단위, 정수)
        """
        self.name = name
        self.ingredients = ingredients  # 재료 목록은 리스트로 관리
        self.cooking_time = cooking_time
    
    def add_ingredient(self, ingredient):
        """재료 추가 (중복 없이 추가)"""
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            print(f"{ingredient} 추가됨.")
        else:
            print(f"{ingredient}은(는) 이미 존재합니다.")
    
    def remove_ingredient(self, ingredient):
        """재료 제거"""
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            print(f"{ingredient} 제거됨.")
        else:
            print(f"{ingredient}은(는) 목록에 없습니다.")
    
    def display_recipe(self):
        """현재 레시피의 모든 정보 출력"""
        print("레시피 이름:", self.name)
        print("재료 목록:", ", ".join(self.ingredients))
        print("조리 시간:", self.cooking_time, "분")
    
    def calculate_difficulty(self):
        """
        재료의 수와 조리 시간을 고려하여 난이도를 계산합니다.
        예시 기준:
          - 조리 시간이 30분 이하이고 재료가 5개 이하이면 '쉬움'
          - 조리 시간이 60분 이하이고 재료가 10개 이하이면 '보통'
          - 그 외는 '어려움'
        """
        num_ingredients = len(self.ingredients)
        if self.cooking_time <= 30 and num_ingredients <= 5:
            return "쉬움"
        elif self.cooking_time <= 60 and num_ingredients <= 10:
            return "보통"
        else:
            return "어려움"


if __name__ == '__main__':
    my_recipe = Recipe("파스타", ["면", "토마토 소스", "치즈"], 25)
    my_recipe.display_recipe()
    print("난이도:", my_recipe.calculate_difficulty())
    my_recipe.add_ingredient("바질")
    my_recipe.remove_ingredient("치즈")
    my_recipe.display_recipe()
    print("난이도:", my_recipe.calculate_difficulty())