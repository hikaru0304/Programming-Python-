class resturant:
    def __init__(self, name, theatername, kind):
        # 식당 이름
        self.name = name
        # 음식 종류
        self.kind = kind
        # 메뉴
        self.menu = {}
        # 주소
        self.location = ''

  def set_link(self):
        link = input('>> 레시피 영상 주소를 입력하세요: ')
        self.link = '입력된 주소가 없다' if link == '' else link
    def set_info(self):
        info = input('>> 레시피 정보를 입력하세요:')
        self.info = '입력된 주소가 없어요' if info == '' else info


    def set_quantity(self):
        quantity = input('>> 레시피가 몇 인분 기준인가요?: ')
        self.quantity = quantity
        self.quantity = 1 if quantity == '' else quantity

    def set_time(self):
        time = input('>> 레시피 소요시간을 입력하세요 : ')
        self.time = 0 if time == '' else time
    def set_whatin(self):
        while True:
            whatin = input('>>> 재료를 입력하세요(예시 감자 100): (입력이 끝나면 enter를 치세요)')
            if whatin == '':
                break
            name, gram = whatin.split()
            self.whatin[name] = gram + 'g'
    def set_recipe(self):
        self.set_link()
        self.set_whatin()
        self.set_time()
        self.set_info()
        self.set_quantity()


    def __str__(self):
        return f'레시피: {self.name}\n양: {self.quantity}인분\n정보:{self.info}\n링크:{self.link}' \
              f'재료:{self.whatin}\n 시간:{self.time}'
class Choice_Resturant:
    def __init__(self):
        self.광림아트센터 = []
    def 광림아트센터(self):
        자미당 = resturant("자미당 압구정점", "디저트")
        자미당.menu = {'꽈배기(3개) : 2000원', '찹살도너츠(3개(개):2000원', }
        자미당.location = '서울 강남구 논현로 851 1층 자미당'

        담미온 = resturant('담미온 압구정점', '한식')
        담미온.menu = {'수육국밥(보통) 8000원', '순대국밥(보통) 8000원'}
        담미온.location = '서울 강남구 압구정로 28길 42'

        시골밥상 = resturant('시골밥상', '한식')
        시골밥상.menu = {'갈치조림정식 9000원', '시골밥상 8000원', '불고기 12000원', '돈목살구이 11000원'}

        스파게티스토리 = resturant('스파게티스토리' '양식')
        스파게티스토리.menu = {'미트소스스파게티 4500원', '토마토소스 스파게티 4500원'}
