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
#
# phone_number = "02-1234-5678"
# phone_number2 = "032-9876-4321" #[:3]
# x = phone_number.index('-') #없으면 valueError, find()없으면 -1
# # x = phone_number.find('?')
# print(phone_number[0:x]) #[:2]
# print(phone_number[-4:])
#
# # 전화번호 입력시, -가 있든, -가 없든 찰떡같이 알아먹기
# phone_number1 = '010-1234-5678'
# phone_number2 = '01098765432'
# phone_number3 = '010 1111 2222'
# phone_number = phone_number3
# result = phone_number1.replace('-','').replace(' ','')
# print(result)
# result = phone_number3.replace(' ','')
# print(result)
# # Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# # 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# # student_number = '2100' 또는 student_number = '2000'
# # <출력 예시>
# # 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
# student_number="2100"
# number=student_number[1] #[1:2]    #'3'
# number=int(number) #str -> int
# # if number==1:
# #     print(f"{number}반 뉴미디어소프트웨어과")
# # elif number==2:
# #     print(f"{number}반 뉴미디어소프트웨어과")
# # elif number==3:
# #     print(f"{number}반 뉴미디어웹솔루션과")
# # elif number==4:
# #     print(f"{number}반 뉴미디어웹솔루션과")
# # elif number==5:
# #     print(f"{number}반 뉴미디어디자인과")
# # elif number==6:
# #     print(f"{number}반 뉴미디어디자인과")
# # else:
# #     print("잘못입력했습니다.")
# # majors = ['뉴미디어소프트웨어과','뉴미디어소프트웨어과','뉴미디어웹솔루션과','뉴미디어웹솔루션과','뉴미디어디자인과','뉴미디어디자인과']
# # print(f'{number}반 {majors[number-1]}')
#
# majors = ['뉴미디어소프트웨어과','뉴미디어웹솔루션과','뉴미디어디자인과']
# if 1 <= number <= 6:    #1 <= number && number <= 6 in java
#     print(f'{number}반 {majors[(number-1) // 2]}')
# else :
#     print("잘못 입력했습니다")
# # Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# # <함수 호출>
# # grade, major = get_major('2100')
# # print(major, grade) #뉴미디어소프트웨어과 2
# # def info(grade,major):
# #     print("학년 : {0}\t 학과: {1}\t"
# #           .format(grade,major))
# # # info("2학년","웹솔루션")
# # def get_major(student_number):
# #     global major
# #     grade = student_number[0]
# #     if student_number[1] == '1' or student_number[1] == '2':
# #         major = "뉴미디어소프트웨어과"
# #     elif student_number[2] == '3' or student_number[1] == '4':
# #         major ="뉴미디어웹솔루션과"
# #     elif student_number[3] == '5' or student_number[1] == '6':
# #         major ="뉴미디어디자인과"
# #     return grade, major
# # grade,major = get_major("2510")
# # print(major,grade)
# # Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# # <함수 호출>
# # print(average(10, 20, 30)) #20.0
# # print(average(4, 23)) #13.5
# n = int(input("넣을 수를 입력해주세요"))
# total =0
# for i in range(n) :
#     total = total + float(input("숫자를 입력해주세요"))
# print(total/n)
# # Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# # (소수 첫째자리까지 반올림)
# # * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# # 18.5 미만: 저체중
# # 18.5 이상 23 미만: 보통
# # 23 이상 25 미만: 과체중
# # 25 이상: 비만
# # <함수 호출>
# # bmi = get_bmi(176, 69)
# # print(bmi) #22.3
# height=170
# weight=55
# bmi=round(weight/((height/100)*(height/100)))
# def bmi_info():
#    if bmi<18.5 :
#        return "저체중"
#    elif bmi<23 :
#        return "보통"
#    elif bmi<25:
#        return "과체중"
#    elif bmi>26:
#        return "비만"
# print("당신의 bmi지수는 {0}입니다 그래서 {1}입니다.".format(bmi,bmi_info()))
# # print(bmi_info(168,55))
# # Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
# # '''
# # result = n_sum(10)
# # print(result)        #1
# # result = n_sum(331)
# # print(result)         #7
# # result = n_sum(408)
# # print(result)         #12
# # result = n_sum(1000000000)
# # print(result)         #-1
# def n_sum(number):
#   sum = 0
#   i = number
#   while i >0:
#       sum += i%10
#       i = (int)(i/10)
#       if i >1000000000:
#         i *= -1
#   return sum
# print("자릿수의 합은 {0}".format(n_sum(123)))
# # Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# # * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
# # '''
# # fare = get_subway_fare(5)
# # print(fare)        #720
# # fare = get_subway_fare(26)
# # print(fare)        #1120
# # fare = get_subway_fare(61)
# # print(fare)        #1720
# #fare = 요금
# # distance =" 5"
# # fare =" 0"
# distance = int(input("간 거리를 입력하시오: "))
# def get_subway_fare():
#     if distance<11:
#         fare = 720
#         return fare
#     elif distance<50:
#         bonus=distance-10
#         more=(bonus%5)*100
#         fare =720 + ((bonus// 5)*100)+more
#         return fare
#     else:
#         bonus = distance-9
#         more = (bonus % 8) * 100
#         fare = 720 + ((bonus// 8)*100)+more
#         return fare
# print("요금은 {0}".format(get_subway_fare()))
# # # '''
# # Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# # * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# # '''
# # result = get_three_six_nine(1)
# # print(result)        #1
# # result = get_three_six_nine(3)
# # print(result)        #짝
# # result = get_three_six_nine(16)
# # print(result)        #짝
# # result = get_three_six_nine(36)
# # print(result)        #짝짝
# i = input("숫자를 입력하시오 : ")
# def get_three_six_nine():
#     if i<"10" or "3" in i or "6" in i or "9" in i:
#        return "짝"
#     elif i > "10" and "3" in i and "6" in i and "9" and i:
#         return "짝짝"
#     else:
#         return i
# print("{0}".format(get_three_six_nine()))
# # ''
# # Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# # 1. 함수의 이름을 정해준다.
# # 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# # 3. 리턴하는 것을 말해준다.
# # 4. 출력 예시를 보여준다.
# # 5. 내가 낸 문제의 답안을 제출한다.
# # # '''
# # score란 변수에 점수를 입력받는다.
# # show라는 함수를 생성한다.
# # 90점 이상이면 A 80점이상이면 B 70점 이상이면 C 60점 이상이면 D 그외에는 F로 출력한다.
# # 학점을 return 한다.
# score = int(input("점수를 입력해주세요 : "))
# def show():
#     if score >=90:
#         grade = "A"
#         return grade
#     elif score >=80:
#         grade= "B"
#         return grade
#     elif score>=70:
#         grade = "C"
#         return grade
#     elif score>=60:
#         grade = "D"
#         return grade
#     else:
#         grade = "F"
#         return grade
# print("{0}".format(show()))