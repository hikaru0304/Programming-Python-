class Entertainer:  #키, 얼굴, 인성, 이름
    def __init__(self,name):
        self.name = name

    def set_height(self,height):
        self.height=height
    def set_face(self, face):
        self.face = face
    def set_kind(self,kind): #인성
        self.kind = kind
    def set_name(self,name):
        self.name = name
    # def info(self):
    #     print(f'이름: {self.name}')
    def __str__(self):
        return f'이름:{self.name}\t 키: {self.height}\t얼굴: {self.face}\t인성:{self.kind}'

# 아이유 = Entertainer('아이유')
# # 아이유.set_name('아이유')
# # 아이유.set_name('이지은')
# 아이유.set_height('161cm')
# 아이유.set_face('형섭쌤이상형')
# 아이유.set_kind('That\'s very good')
# print(아이유)
# # 아이유.info()

태민 = Entertainer('태민')
태민.set_height('174cm')
태민.set_face('요정')

태민.set_kind('조용하면서도 열정적이고 완벽함을 보여주는 사람이다.')
print(태민)
태민.set_name('이태민')

class Singer(Entertainer):
    def __init__(self,name,song):
        super().__init__(name)  #self.name = name
        self.song = song
    def __str__(self):
        return super().__str__() + f'\t대표곡:{self.song}'
class Talent(Entertainer):
    def __init__(self,name,drama):
        super().__init__(name)
        self.drama = drama
    def __str__(self):
        return super().__str__()+f'\t드라마:{self.drama}'

태민 = Singer('태민','Criminal')
태민.set_height('174cm')
태민.set_face('요정')

태민.set_kind('조용하면서도 열정적이고 완벽함을 보여주는 사람이다.')
print(태민)

키 = Singer('키','Forever yours')     #new라는 객체를 안쓴다.
키.set_height('176cm')
키.set_face('햄스터닮은 여우')

키.set_kind('자기 주관이 뚜렷하며 자신이 어떻게 나아가고 싶은지 확고한 신념을 갖고 있다..')
print(키)

샤이니 = []
샤이니.append(태민)
샤이니.append(키)
print(샤이니)


김소연 = Talent('김소연','펜트하우스')
김소연.set_height('164cm')
김소연.set_face('매혹적인 얼굴')
김소연.set_kind('천사')
print(김소연)
