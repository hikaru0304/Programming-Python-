class Theater:
    def __init__(self,name,scale):
        #극장 이름
        self.name = ''
        #규모
        self.scale = ''
        #지하철 역
        self.station = ''
        self.grand_theater_list=[]
    def grandtheater(self):
        광림아트센터 = Theater('광림아트센터BBC홀', '대극장')
        광림아트센터.station = '압구정역'
        self.grand_theater_list.append(광림아트센터)

        디큐브아트센터 = Theater('디큐브아트센터', '대극장')
        디큐브아트센터.station = '신도림역'
        self.grand_theater_list.append(디큐브아트센터)

        블루스퀘어 = Theater('블루스퀘어 신한카드홀', '대극장')
        블루스퀘어.station = '한강진역'
        self.grand_theater_list.append(블루스퀘어)

        세종문화회관대극장 = Theater('세종문화회관 대극장', '대극장')
        세종문화회관대극장.station = '광화문역'
        self.grand_theater_list.append(세종문화회관대극장)

        예술의전당오페라 = Theater('예술의전당 오페라극장', '대극장')
        예술의전당오페라.station = '남부터미널역'
        self.grand_theater_list.append(예술의전당오페라)

        예술의전당토월 = Theater('예술의전당 CJ 토월극장', '대극장')
        예술의전당토월.station = '남부터미널역'
        self.grand_theater_list.append(예술의전당토월)

        예술의전당토월 = Theater('예술의전당 CJ 토월극장', '대극장')
        예술의전당토월.station = '남부터미널역'
        self.grand_theater_list.append(예술의전당토월)

        유니버설아트센터 = Theater('유니버설아트센터', '대극장')
        유니버설아트센터.station = '아차산역'
        self.grand_theater_list.append(유니버설아트센터)

        충무아트센터 = Theater('충무아트센터 대극장', '대극장')
        충무아트센터.station = '신당역'
        self.grand_theater_list.append(충무아트센터)

        한전아트센터 = Theater('한전아트센터', '대극장')
        한전아트센터.station = '양재역'
        self.grand_theater_list.append(한전아트센터)
    def medium_theater(self):
        pass
    def small_theater(self):
        pass
    def Daehak_ro(self):
        pass



