# # 3. Quiz
# # 3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# # 출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력
# # 예시
# # id_number = 020316 일 때
# #
# # 출력 예시
# # 02
# # 0316
# # 732
# #3-1
# id_number = "020316"
# print(id_number[0:2])
# print(id_number[2:])
# front = int(id_number[0:2])
# back = int(id_number[2:])
# print(front+back)
# # 3-2. 집 전화번호를 phone_number에 넣고,
# # 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# # 예시
# # phone_number = 02-1234-5678 또는 032-9876-4321
# #
# # 출력 예시
# # 02 또는 032
# # 5678 또는 4321
# #3-2
# phone_number = "02-1234-5678"
# # phone_number = "032 - 9876 - 4321"
# print(phone_number[0:2])
# print(phone_number[13:])
#
# id_number = "020316" #[2:], [-4:]
# year = id_number[0:2]
# month_day = id_number[2:6]
# print(year)
# print(month_day)
# print(int(year) * int(month_day))
#
# phone_number = "02-1234-5678"
# print(phone_number[0:2]) #[:2]
# print(phone_number[-4:])
#
# phone_number2 = "032-9876-4321" #[:3]
# print(phone_number2[0:3])
# print(phone_number2[-4:])
#
# # 인수에 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# # print(average(10,20,30)) => 20.0
# # print(average(4,23)) => 13.5
#
# # 평균 = 더한만큼/그 갯수를 나눈다 = 총합/갯수
# def average(*numbers):
#     #*을 붙이면 갯수가 아무거나 들어와도 상관이 없다.
#     sum_value = 0
#     count = 0
#     for number in numbers:
#         sum_value += number
#         count += 1
#     return sum_value / count
# print(average(10,20,30))
#
# def average2(*numbers):
#     return sum(numbers) / len(numbers)
#
# print(average2(10,20,30))
# print(average2(4,23))
#
# # 4.키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# # (소수 첫째자리까지 반올림)
# # *BMI 지수 계산법: 체중(kg) / 키의 제곱(m^2)
# #
# #     함수호출
# #     bmi = get_bmi(176,69)
# #     print(bmi)
# def get_bmi(height,weight):
#     height/= 100
#     return round(weight / (height ** 2),1)
#
# bmi = get_bmi(176,69)
# # print(bmi)
# if bmi < 18.5:
#     print('저체중')
# elif 18.5<=bmi<23:
#     print('정상')
# elif 23 <= bmi < 25:
#     print('과체중')
# elif 25<=bmi:
#     print('비만')
#
# # 구구단 7단 출력하기
# # dan:2~9
# for dan in range(2,9+1): # i:1~9
#     for i in range(1,9+1):
#         # if
#         if i % 2 ==0:
#             continue
#         print(f'{dan}x{i}={dan*i}')
#         # print('-' * 10) 각 줄마다 단이 쳐진다.
#     print('-' * 10)
#     if dan == 7:
#         break
 # print('-' * 10) 다 출력하고 맨 마지막에 단이 쳐진다.

# Quiz 4-1 [학생퀴즈] 소수판별하기(소수 : 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime()함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면"소수 아님"리턴한다.
'''
result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님

#
# '''
# import result as result
#
#
# def is_prime(number):
#   for i in range(2,number-1):
#       result = number%i
#       if result == 0:
#             return "소수아님"
#   else:
#       return "소수"
# result = is_prime(36)
# print(result)
# result = is_prime(13)
# print(result)
# result = is_prime(2)
# print(result)
#
# # Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다.
# # 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
# # '고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# # '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
# # '''
# # result = get_compliment('고구마 된장국')
# # print(result) # 왓쇼이!
# # result = get_compliment('맛있는 크레이프')
# # print(result) # 우마이!
# # result = get_compliment('놀랄 만한 상황')
# # print(result) # 요모야..!
# # result = get_compliment('좋은 마음가짐이다!')
# # print(result) # 으무!
# def get_compliment(text_str):
#     if text_str.count("고구마"):
#         return "왓쇼이!"
#     elif text_str.count("맛있는"):
#         return "우마이!"
#     elif text_str.count("놀랄 만한"):
#         return "오모야!"
#     else:
#         return "으무!"
# result = get_compliment("고구마 된장국")
# print(result)
# result = get_compliment("맛있는 크레이프")
# print(result)
# result = get_compliment("놀랄 만한 상황")
# print(result)
# result = get_compliment("좋은 마음가짐이다!")
# print(result)
# Quiz 5-1 모듈이란?
# A.모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다. 모듈은 다른 파이썬 프로그램에서
# 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있따.
# Quiz 5-2 패키지란?
# A.패키지는 특정 기능과 관련된 여러 모듈을 하나의 상위폴더에 넣어놓은 것이다.
# Quiz5-3. theather_module.py 모듈(파일)의 price함수를 p학번이라는 이름으로 호출 하도록 import 문을 작성하세요
# A.import theater_module as p학번
# Quiz5-4.__all__의 역할은?
# A.패키지 안에서 'import *'로 사용하고 싶다면 __init__.py파일 안의 __all__변수에 *로 선언할 때 호출할 모듈들을
# 선언해줘야 한다.
# Quiz 5-5.지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행 되지 않도록 하는
# 제어문은?
# A.if__name__=="__main__":
#      pass
# Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail
# 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
# import travel.vietnam
# < 가 >
# trip_to = travel.vietnam.VietnamPackage()
# trip_to.detail()
#
# from travel import vietnam
# < 나 >
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
#
# from travel.vietnam import ThailandPackage
# < 다 >
# trip_to = ThailandPackage()
# trip_to.detail()