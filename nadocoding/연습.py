def prime_number(number):
    if number != 1:
        for f in range(2,number):
            if number % f ==0:
                return False
    else:
        return False
    return True
num = input("숫자를 입력하세요 : ")
if prime_number(int(num)):
    print(num+"은 소수 입니다.")
else:
    print(num+"은 소수가 아닙니다.")