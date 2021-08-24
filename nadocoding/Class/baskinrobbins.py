class Icecream:
    def __init__(self,name,flavor):
       self.name = name
       self.flavor = flavor
    # 이름:name 맛:flavor, 설명:description
    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f'이름: {self.name}\t맛:{self.flavor}'


# 트리플민초 = Icecream('트리플민초','3배강한 민트초코 맛')
# 트리플민초.set_description('민초의 끝판왕! 기존의 민트 초콜릿 대비 3배 이상 강력한 민트 초코 아이스크림')
# print(트리플민초)
# print(트리플민초.description)
#
# 해피버스데이 = Icecream('해피 버스데이','케이크맛')
# 해피버스데이.set_description('케이크맛 아이스크림, 바닐라향 아이스크림에 레인보우 스프링클스와 케이크 큐브가 쏙쏙')
# print(해피버스데이)
# print(해피버스데이.description)
#
# 슈팅스타 = Icecream('슈팅스타','팝핑캔디')
# 슈팅스타.set_description('톡톡 터지는 팝핑 캔디와 스프링클 캔디, 상크한 체리 시럽이 들어있는 제품')
# print(슈팅스타)
# print(슈팅스타.description)

class Cup:
    _CUP_CATEGORIES = ['싱글컵','더블컵','파인트']
    _PRICES = [4000,6200,8200]
    # CUP_CATEGORIES[self.count_flavor-1]
    def __init__(self,name,price,count_flavor):
        self.name = name
        self.price = price
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor-1]
        self.menu = []
        self.add_menu()
        self.order_menu = []
    def add_menu(self):
        트리플민초 = Icecream('트리플민초', '3배강한 민트초코 맛')
        해피버스데이 = Icecream('해피 버스데이', '케이크맛')
        슈팅스타 = Icecream('슈팅스타', '팝핑캔디')
        self.menu.append(트리플민초)
        self.menu.append(해피버스데이)
        self.menu.append(슈팅스타)
    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index+1,icecream)
    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()                #메뉴 보여주기
            flavor = input('맛을 고르세요 : ')    #사용자 선택
            flavor = int(flavor)    #인덱스를 위해 문자 -> 숫자
            icecream = self.menu[flavor-1]  #메뉴에서 인덱스로 가져오자
            self.order_menu.append(icecream)    #주문한 메뉴에 추가하자
        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu:    #주문내역 보여주자
            print(icecream)
    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t 종류: {Cup._CUP_CATEGORIES[self.count_flavor-1]}\t'

# 이지꺼 = Cup('더블컵',6200,2)
# print(이지꺼)
# 이지꺼.order()

나현이꺼 = Cup('싱글컵',4000,1)
나현이꺼.order()
print(나현이꺼)

