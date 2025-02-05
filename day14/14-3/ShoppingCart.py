class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """상품 추가"""
        self.items.append(item)
        print(f"{item['name']} 추가됨.")
    
    def remove_item(self, item_name):
        """상품 이름으로 해당 상품 제거 (제거되면 True, 없으면 False 반환)"""
        for i, item in enumerate(self.items):
            if item.get('name') == item_name:
                del self.items[i]
                print(f"{item_name} 제거됨.")
                return True
        print(f"{item_name}을(를) 찾을 수 없습니다.")
        return False
    
    def calculate_total(self):
        """총 금액 계산"""
        total = sum(item.get('price', 0) for item in self.items)
        return total

if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item({'name': '사과', 'price': 1000})
    cart.add_item({'name': '바나나', 'price': 1500})
    cart.remove_item('사과')
    print("총 금액:", cart.calculate_total())