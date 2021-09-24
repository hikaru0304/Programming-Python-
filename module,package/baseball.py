from baseball_game_engine import make_quiz, check
from custom_error import InvalidCountError
answer = make_quiz()

# 무한반복
while True:
# 숫자3자리 중복없이 묻자
    player = input("숫자 세자리는?")  #player: "123" "fun"
    try:    #숫자가 아닐 때 예외 처리
        player_int = int(player)    #ValueError
    except ValueError:
        continue
    #길이가 3이 아닐 때 예외 처리
    if len(player) != len(answer):
        #raise InvalidCountError("3자리가 아닙니다.")
        print(f'입력한 숫자의 개수가 정답과 다릅니다.정답:{len(answer)}글자')
        continue
# strike, ball 확인하자
    strike,ball = check(answer,player)
# 출력하자
    print(f'{player}\tstrike:{strike}\tball:{ball}')
# strike가 3일 때, 나가자
    if strike == 3:
        break
# 축하해주자
print('축하합니다. 👏👏👏')
