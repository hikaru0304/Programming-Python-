# # # 숫자 자료형 2-1
# # import self as self
# #
# # print(5)
# # print(-10)
# # print(3.14)
# # print(1000)
# # print(5 + 3)
# # print(2 * 8)
# # print(3 * (3 + 1))
# # # 문자열 자료형 2-2
# # print('풍선')
# # print("나비")
# # print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# # print("ㅋ" * 9)
# # # 2 - 3 boolean 자료형
# # print(5 > 10)
# # print(5 < 10)
# # print(True)
# # print(False)
# # print(not True)
# # print(not False)
# # print(not (5 > 10))
# # # 애완동물을 소개해주세요~
# # # 2-4 변수
# # animal = "고양이"
# # name = "해피"
# # age = 4
# # hobby = "낮잠"
# # is_adult = age >= 3
# #
# # print("우리집" + animal + "의 이름은" + name + "예요")
# # hobby = "공놀이";
# # print(name + " 는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")
# # print(name + "는 어른일까요?" + str(is_adult))
# #
# # # 2-5 주석
# # # print("우리집"+ animal+ "의 이름은"+ name + "예요")
# # # hobby = "공놀이";
# # # print(name + " 는 " +str(age)+"살이며,"+hobby+"을 아주 좋아해요")
# # # print(name + "는 어른일까요?"+ str(is_adult))
# #
# # # 2-6. Quiz #1
# # # Quiz) 변수를 이용하여 다음 문장을 출력하시오
# # #
# # # 변수명: station
# # # 변수값 : "사당","신도림","인천공항" 순서대로 출력
# # # 출력 문장 : XX행 열차가 들어오고 있습니다.
# #
# # station = "인천공항"
# # print(station + "행 열차가 들어오고 있습니다.")
# #
# # # 3-1. 연산자
# # print(1 + 1)  # 2
# # print(3 - 2)  # 1
# # print(5 * 2)  # 10
# # print(6 / 3)  # 2
# #
# # print(2 ** 3)  # 2^3 = 8
# # print(5 % 3)  # 나머지 구하기 2
# # print(10 % 3)  # 1
# # print(5 // 3)  # 1
# # print(10 // 3)  # 3
# #
# # print(10 > 3)  # True
# # print(4 >= 7)  # False
# # print(10 < 3)  # False
# # print(5 <= 5)  # True
# #
# # print(3 == 3)  # True
# # print(4 == 2)  # False
# # print(3 + 4 == 7)  # True
# # print(1 != 3)  # True
# # print(not (1 != 3))  # False
# #
# # print((3 > 0) and (3 < 5))  # True
# # print((3 > 0) & (3 < 5))  # True
# #
# # print((3 > 0) or (3 > 5))  # True
# # print((3 > 0) | (3 > 5))  # True
# #
# # print(5 > 4 > 3)  # True
# # # 3-2 간단한 수식
# # print(2 + 3 * 4)  # 14
# # print((2 + 3) * 4)  # 20
# # number = 2 + 3 * 4
# # print(number)
# # number = number + 2  # 16
# # print(number)
# # number += 2  # 18
# # print(number)
# # number *= 2  # 36
# # print(number)
# # number /= 2  # 18
# # print(number)
# # number -= 2  # 16
# # print(number)
# # number %= 2  # 0
# # print(number)
# # # 3-3 숫자 처리 함수
# # print(abs(-5))  # 5
# # print(pow(4, 2))  # 4^2 = 4*4 = 16
# # print(max(5, 12))  # 12
# # print(min(5, 12))  # 5
# # print(round(3.14))  # 3
# # print(round(4.99))  # 5
# #
# # from math import *
# #
# # print(floor(4.99))  # 내림. 4
# # print(ceil(3.14))  # 올림 . 4
# # print(sqrt(16))  # 제곱근 . 4
# #
# # # 3-4 랜덤 함수
# # from random import *
# #
# # print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
# # print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
# # print(int(random() * 10))  # 0.0~10.0 미만의 임의의 값 생성
# # print(int(random() * 10))  # 0.0~10.0 미만의 임의의 값 생성
# # print(int(random() * 10))  # 0.0~10.0 미만의 임의의 값 생성
# # print(int(random() * 10) + 1)  # 1.0~10.0 이하의 임의의 값 생성
# # print(int(random() * 10) + 1)  # 1.0~10.0 이하의 임의의 값 생성
# # print(int(random() * 10) + 1)  # 1.0~10.0 이하의 임의의 값 생성
# # print(int(random() * 10) + 1)  # 1.0~10.0 이하의 임의의 값 생성
# # print(int(random() * 10) + 1)  # 1.0~10.0 이하의 임의의 값 생성
# # print(int(random() * 10) + 1)  # 1.0~10.0 이하의 임의의 값 생성
# #
# # print(int(random() * 45) + 1)  # 1~45이하의 임의의 값 생성
# # print(int(random() * 45) + 1)  # 1~45이하의 임의의 값 생성
# # print(int(random() * 45) + 1)  # 1~45이하의 임의의 값 생성
# # print(int(random() * 45) + 1)  # 1~45이하의 임의의 값 생성
# # print(int(random() * 45) + 1)  # 1~45이하의 임의의 값 생성
# # print(int(random() * 45) + 1)  # 1~45이하의 임의의 값 생성
# #
# # print(randrange(1, 46))  # 1 ~46 미만의 임의의 값 생성
# # print(randrange(1, 46))  # 1 ~46 미만의 임의의 값 생성
# # print(randrange(1, 46))  # 1 ~46 미만의 임의의 값 생성
# # print(randrange(1, 46))  # 1 ~46 미만의 임의의 값 생성
# # print(randrange(1, 46))  # 1 ~46 미만의 임의의 값 생성
# # print(randrange(1, 46))  # 1 ~46 미만의 임의의 값 생성
# #
# # print(randint(1, 45)) # 1~ 45이하의 임의의 값 생성
# # print(randint(1, 45)) # 1~ 45이하의 임의의 값 생성
# # print(randint(1, 45)) # 1~ 45이하의 임의의 값 생성
# # print(randint(1, 45)) # 1~ 45이하의 임의의 값 생성
# # print(randint(1, 45)) # 1~ 45이하의 임의의 값 생성
# # print(randint(1, 45)) # 1~ 45이하의 임의의 값 생성
# #
# # #Quiz 2
# # # 당신의 최근에 코딩 스터디 모임을 새로 만들었습니다
# # # 우러 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다
# # # 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오..
# # # 조건1 : 랜덤으로 날짜를 뽑아야함
# # # 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# # # 조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외
# # #
# # # (출력문 예제)
# # # 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
# #
# # from random import *
# # date = randint(4,28)
# # print("오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다." + str(date) + "일로 선정되었습니다.")
# #
# # #4 - 1 문자열
# # sentence = '나는 소년입니다.'
# # print(sentence)
# # sentence2 = "파이썬은 쉬워요"
# # print(sentence2)
# # sentence3 = """
# # 나는 소년이고,
# # 파이썬은 쉬워요
# # """
# # print(sentence3)
# #
# # #4 - 2 슬라이싱
# # jumin = "990120-1234567"
# #
# # print("성별 : " +jumin[7])
# # print("연 : " + jumin[0:2]) #0부터 2직전까지
# # print("월 : " + jumin[2:4])
# # print("일 : " + jumin[4:6])
# # print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
# # print("뒤 7자리 : " + jumin[7:14])
# # #print("뒤 7자리 : " + jumin[7:]) 7부터 끝까지
# # print("뒤 7자리(뒤에서부터) : " + jumin[-7:])
# # # 맨 뒤에서 7번째부터 끝까지
# #
# # # 4-3 문자열 처리 함수
# # python = "Python is Amazing"
# # print(python.lower())
# # print(python.upper())
# # print(python[0].isupper)
# # print(len(python))
# # print(python.replace("Python", "Java"))
# #
# # index = python.index("n")
# # print(index)
# # index = python.index("n", index + 1)
# # print(index)
# #
# # print(python.find("n"))
# # print(python.find("Java"))
# # # print(python.index("Java"))
# # print("hi")
# # print(python.count("n"))
# #
# # #4-4 문자열포맷
# # # print("a" + "b")
# # # print("a", "b")
# #
# # #방법1
# # print("나는 %d살입니다." % 20)
# # print("나는 %s을 좋아해요." % "파이썬")
# # print("Apple은 %c로 시작해요." %"A")
# # # %s
# # # print("나는 %s살입니다." %20)
# # # print("나는 %s 색과 %s 색을 좋아해요." %("파란", "빨간"))
# # #방법 2
# # print("나는 {}살입니다." .format(20))
# # print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# # print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
# # print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
# #
# # #방법 3
# # # print("나는 {}살이며, {}색을 좋아해요".format(age = 20 , color="빨간"))
# # print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))
# #
# # #방법 4
# # age = 20
# # color = "빨간"
# # print(f"나는 {age}살이며, {color}색을 좋아해요.")
# # #
# # # 4-5 탈출문자
# # print("백문이 불여일견 백견이 불여일타")
# # # print("백문이 불여일견 "
# # #       "백견이 불여일타")
# # # \n : 줄바꿈
# # # 저는 "나도코딩"입니다
# # print("저는 나도코딩입니다")
# # # print("저는 "나도코딩"입니다")
# # print("저는 '나도코딩'입니다")
# #
# # print("저는\"나도코딩\"입니다.")
# # print("저는\'나도코딩\'입니다.")
# #
# # # \\ : 문장 내애서 \
# # print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")
# # # \r : 커서를 맨 앞으로 이동
# # print("Red Apple\rPine")
# #
# # # \b : 백스페이스 ( 한 글자 삭제)
# # print("Redd\bApple")
# #
# # # \t : 탭
# # print("Red\tApple")
# #
# # # Quiz #3
# # # Quiz)사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# # # 예)http://naver.com
# # # 규칙1: http:// 부분은 제외 => naver.com
# # # 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# # # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# # #         (nav)                   (5)         (1)             (!)
# # # 예) 생성된 비밀번호 : nav51!
# # # url = "http://naver.com"
# # # # url = "http://daum.com"
# # # url = "http://google.com"
# # url = "http: // youtube.com"
# #
# # my_str = url.replace("http : //", "") #규칙1
# # # print(my_str)
# # my_str = my_str[:my_str.index(".")] #my_str[0:5] - > 0~5직전까지 ( 0,1,2,3,4)
# # # print(my_str)
# # password = my_str[:3] +str(len(my_str)) + str(my_str.count("e")) + "!"
# # print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
# #
# # # 5 - 1 리스트 []
# # # 지하철 칸별로 10명, 20명, 30명
# # # subway1 = 10
# # # subway2 = 20
# # # subway3 = 30
# # subway = [10,20,30]
# # print(subway)
# #
# # subway = ["유재석", "조세호", "박명수"]
# # print(subway)
# #
# # # 조세호가 몇 번째 칸에 타고 있는가?
# # print(subway.index("조세호"))
# #
# # # 하하씨가 다음 정류장에서 다음 칸에 탐
# # subway.append("하하")
# # print(subway)
# #
# # # 정형돈씨를 유재석/조세호 사이에 태워봄
# # subway.insert(1,"정형돈")
# # print(subway)
# #
# # # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# # print(subway.pop())
# # print(subway)
# #
# # # print(subway.pop())
# # # print(subway)
# # #
# # # print(subway.pop())
# # # print(subway)
# #
# # # 같은 이름의 사람이 몇 명 있는 지 확인
# # subway.append("유재석")
# # print(subway)
# # print(subway.count("유재석"))
# #
# # # 정렬도 가능
# # num_list = [5,2,4,3,1]
# # num_list.sort()
# # print(num_list)
# #
# # # 뒤집기도 가능
# # num_list.reverse()
# # print(num_list)
# #
# # # 모두 지우기
# # num_list.clear()
# # print(num_list)
# #
# # # 다양한 자료형 함께 사용
# # num_list = [5,2,4,3,1]
# # mix_list = ["조세호",20,True]
# # print(mix_list)
# #
# # # 리스트 확장
# # num_list.extend(mix_list)
# # print(num_list)
# #
# # # 5 - 2 사전
# # # cabinet = {3 : "유재석", 100:"김태호"}
# # # print(cabinet[3])
# # # print(cabinet[100])
# #
# # # print(cabinet.get(3))
# # # print(cabinet.get[5])
# # # print("hi")
# # # print(cabinet.get(5))
# # # print(cabinet.get(5,"사용 가능"))
# # # print("hi")
# # #
# # # print(3 in cabinet) #True
# # # print(5 in cabinet) #False
# #
# # cabinet = {"A-3" : "유재석", "B-100":"김태호"}
# # print(cabinet["A-3"])
# # print(cabinet["B-100"])
# # #
# # # 새 손님
# # print(cabinet)
# # cabinet["A-3"] = "김종국"
# # cabinet["C-20"] = "조세호"
# # print(cabinet)
# #
# # # 간 손님
# # del cabinet["A-3"]
# # print(cabinet)
# #
# # # key 들만 출력
# # print(cabinet.keys())
# #
# # # value 들만 출력
# # print(cabinet.values())
# #
# # # key, value 쌍으로 출력
# # print(cabinet.items())
# #
# # # 목욕탕 매점
# # cabinet.clear()
# # print(cabinet)
# #
# # #5 - 3 튜플
# # menu = ("돈까스","치즈까스")
# # print(menu[0])
# # print(menu[1])
# #
# # # menu.add("생선까스")
# # #
# # # name = "김종국"
# # # age = 20
# # # hobby = "코딩"
# # # print(name,age,hobby)
# #
# # (name, age, hobby) = ("김종국", 20,"코딩")
# # print(name, age, hobby)
# #
# # # 5-4 세트 집합(set)
# # # 중복 안됨, 순서 없음
# # my_set = {1,2,3,3,3}
# # print(my_set)
# #
# # java = {"유재석", "김태호","양세형"}
# # python = {"유재석", "박명수"}
# #
# # # 교집합 (java와 python을 모두 할 수 있는 개발자)
# # print(java&python)
# # print(java.intersection(python))
# #
# # # 합집합(java도 할 수 있거나 python을 할 수있는 개발자)
# # print(java | python)
# # print(java.union(python))
# #
# # # 차집합 ( java 는 할 수 있지만 python은 할 줄 모르는 개발자)
# # # print(java - python)
# # # print(java.difference(python))
# # #
# # # # python 할 줄 아는 사람이 늘어남
# # # print.add("김태호")
# # # print(python)
# # #
# # # # java를 까먹었어요
# # # java.remove("김태호")
# # # print(java)
# #
# # # 5-5자료구조의 변경
# # menu = {"커피", "우유","주스"}
# # print(menu,type(menu))
# # menu = list(menu)
# # print(menu, type(menu))
# # menu = tuple(menu)
# # print(menu, type(menu))
# # menu = set(menu)
# # print(menu, type(menu))
# # # Quiz 4
# # # 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# # # 추첨 프로그램을 작성하시오
# # # 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# # # 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# # # 조건3 : random 모듈의 shuffle 과 sample을 활용
# # # from random import *
# # # lst = [1,2,3,4,5]
# # # # print(lst)
# # # # shuffle(lst)
# # # # print(lst)
# # # print(sample(lst,1))
# #
# # from random import *
# # users = range(1,21) #1부터 20까지 숫자를 생성
# # # print(type(users))
# # users = list(users)
# # # print(type(users))
# #
# # print(users)
# # shuffle(users)
# # print(users)
# #
# # winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피
# #
# # print("---당첨자 발표---")
# # print("치킨 당첨자 : {0}".format(winners[0]))
# # print("커피 당첨자 : {0}".format(winners[1:]))
# # print("---축하합니다---")
# #
# # #6-1 if
# # weather = "비"
# # # if 조건 :
# # if weather == "비" :
# #     print("우산을 챙기세요")
# # weather = "미세먼지"
# # # elif weather == "미세먼지":
# # #     print("마스크를 챙기세요")
#
# #9-1 클래스
# # 마린: 공격 유닛, 군인. 총을 쏠 수 있음
# from random import randint
#
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
#
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# # 탱크2 새로 추가
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
#
# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))
#
# # 공격 함수
# def attack(name, location, damage):
# 	print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))
#
# attack(name, "1시" , damage) # 마린 공격 명령
# attack(tank_name, "1시" , tank_damage) # 탱크 공격 명령
# attack(tank2_name, "1시" , tank2_damage) # 탱크2 공격 명령
# # 9-1 클래스
# #9-2 __init__
# # 9-11 스타크래프트 전반전
# class Unit:
#     def __init__(self, name, hp,speed):
#         self.name = name # 멤버변수 name 에 전달값 name 저장
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name)) #출력문 추가
#     def move(self,location):
#         # print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(self.name,location,self.speed))
#         # print("{0} 유닛이 생성되었습니다.".format(self.name))
#         # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
#     def damaged(self, damage):  # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))  # 데미지 정보 출력
#         self.hp -= damage  # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))  # 남은 체력 출력
#         if self.hp <= 0:  # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name))  # 유닛 파괴 처리
# # 9-3멤버변수
# # 레이스: 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
# # wratih1 = Unit("레이스",80,5) #체력 80, 공격력 5
# # print("유닛 이름 : {0}, 공격력 : {1}".format(wratih1.name,wratih1.damage))
# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# # wraith2 = Unit("빼앗은 레이스", 80, 5)
# # wraith2.cloaking = True # 빼앗은 레이스만을 위한 특별한 멤버변수 정의
# #
# # if wraith2.cloaking == True: # 클로킹 상태라면?
# #     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
#
# # marine1 = Unit("마린", 40, 5)  # 마린1 생성. 전달값으로 name, hp, damage 를 전달
# # marine2 = Unit("마린", 40, 5)  # 마린2 생성
# # tank = Unit("탱크", 150, 35)  # 탱크 생성
# # 9-4 메소드
# # 9-5 상속
# class AttackUnit(Unit): # 공격 유닛
#     def __init__(self, name, hp, speed,damage):
#         Unit.__init__(self, name, hp,speed)
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
#         # 마린
# class Marine(AttackUnit):
#             def __init__(self):
#                 AttackUnit.__init__(self, "마린", 40, 1, 5)  # 이름, 체력, 이동속도, 공격력
#
#             # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#             def stimpack(self):
#                 if self.hp > 10:
#                     self.hp -= 10
#                     print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#                 else:
#                     print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
#
#         # 탱크
# class Tank(AttackUnit):
#             # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#             siege_developed = False  # 시즈모드 개발여부 (클래스 변수)
#
#             def __init__(self):
#                 AttackUnit.__init__(self, "탱크", 150, 1, 35)  # 이름, 체력, 이동속도, 공격력
#                 self.siege_mode = False  # 시즈모드 (해제 상태)
#
#             # 시즈모드
#             def set_siege_mode(self):
#                 if Tank.siege_developed == False:  # 시즈모드가 개발되지 않은 경우 메소드 탈출
#                     return
#
#                 # 현재 시즈모드가 아닐 때
#                 if self.siege_mode == False:
#                     print("{0} : 시즈모드로 전환합니다.".format(self.name))
#                     self.damage *= 2  # 공격력 2배로 증가
#                     self.siege_mode = True  # 시즈 모드 설정
#                 # 현재 시즈모드일 때
#                 else:
#                     print("{0} : 시즈모드를 해제합니다.".format(self.name))
#                     self.damage /= 2  # 공격력 절반으로 감소
#                     self.siege_mode = False  # 시즈 모드 해제
# # 파이어뱃 : 공격 유닛, 화염방사기.
# # firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
# # firebat1.attack("5시") # 5시 방향으로 공격 명령
# #
# # # 공격 2번 받는다고 가정
# # firebat1.damaged(25) # 남은 체력 25
# # firebat1.damaged(25) # 남은 채력 0
#
# # 9-6 다중 상속
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed): # 이름, 체력, 공격력, 공중 이동 속도
#         AttackUnit.__init__(self, name, hp, 0, damage) # 이름, 체력, 공격력
#         Flyable.__init__(self, flying_speed) # 공중 이동 속도
#     def move(self,location):
#         self.fly(self.name,location)
# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
#         self.cloaked = False # 클로킹 모드 (해제 상태)
#
#     # 클로킹 모드
#     def cloaking(self):
#         # 현재 클로킹 모드일 때
#         if self.cloaked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.cloaked = False
#         # 현재 클로킹 모드가 아닐 때
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.cloaked = True
# # 9-8 pass
# # 건물
# # class BuildingUnit(Unit):
# #     def __init__(self, name, hp, location):
# #         pass
#
# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# # supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 체력 500, 생성 위치 7시
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     print("Player : gg") # good game
#     print("[Player]님이 게임에서 퇴장하셨습니다.")
# # 실제 게임 진행
# game_start()
#
# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
#
# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()
#
# # 레이스 1기 생성
# w1 = Wraith()
#
# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t1)
# attack_units.append(w1)
#
# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")
#
# # 탱크 시즈모드 개발
# Tank.siege_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
#
# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine): # Marine 의 인스턴스이면 스팀팩
#         unit.stimpack()
#     elif isinstance(unit, Tank): # Tank 의 인스턴스이면 시즈모드
#         unit.set_siege_mode()
#     elif isinstance(unit, Wraith): # Wraith 의 인스턴스이면 클로킹
#         unit.cloaking()
#
# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")
#
# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)
#
# # 게임 종료
# game_over()
# # # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# # valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) # 이름, 체력, 공격력, 공중 이동 속도
# # valkyrie.fly(valkyrie.name, "3시") # 3시 방향으로 발키리를 이동
#
# # # 벌쳐 : 지상 유닛, 기동성이 좋음
# # vulture = AttackUnit("벌쳐", 80, 10, 20) # 지상 speed 10
# #
# # # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# # battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# #
# # vulture.move("11시")
# # # battlecruiser.fly(battlecruiser.name, "9시")
# # battlecruiser.move("9시") # 오버라이딩된 move() 호출
# #9-9 super
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")
#
#
# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")
#
#
# # class FlyableUnit(Unit, Flyable):
# class FlyableUnit(Flyable, Unit):  # 순서 변경
#     def __init__(self):
#         # super().__init__()
#         Unit.__init__(self)  # Unit 클래스 생성자 호출
#         Flyable.__init__(self)  # Flyable 클래스 생성자 호출
#
#
# # 드랍쉽
# dropship = FlyableUnit()
# # #
# # Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# #
# # (출력 예제)
# # 총 3대의 매물이 있습니다.
# # 강남 아파트 매매 10억 2010년
# # 마포 오피스텔 전세 5억 2007년
# # 송파 빌라 월세 500/50 2000년
# # [코드]
# class House:
#     # 매물 초기화
#     def __init__(self,location,house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location,self.house_type,self.deal_type\
#               , self.price , self.completion_year)
# houses = []
# house1 = House("강남","아파트","매매","10억","2010년")
# house2 = House("마포","오피스텔","전세","5억","2007년")
# house3 = House("송파","빌라","월세","500/50","2000년")
#
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()
# 일반 가격
import theater_module
theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_solider(5) #5명의 군인이 영화 보러 갔을 때

import theater_module as mv
mv.price_solider(3)
mv.price_morning(4)
mv.price_solider(5)

from theater_module import *
# from random import *
price(3)
price_morning(4)
price_solider(5)

from theater_module import price, price_morning
price(5)
price_morning(6)
# price_solider(7)
from theater_module import price_solider as price
price(5)
# 패키지
import nadocoding.thailand
trip_to = nadocoding.thailand.ThailandPackage()
trip_to.detail()

from nadocoding.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from nadocoding import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()

# from random import *
from nadocoding import*
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))