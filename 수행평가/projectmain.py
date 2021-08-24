from 수행평가.theater import Theater


def print_theater():
    print('1. 대극장')
    print('2. 중극장')
    print('3. 소극장')
    print('4. 대학로')
    print('5. 종료')


def main():
    theater = Theater
    while True:
        print_theater()
        theater = input('>> 극장을 선택하세요')
        if theater == '1':
            for index,grand_theater_list  in enumerate(theater,grand_theater_list):
                print()
        elif theater == '2':
            print(f'{index + 1}:{grand_theater_list}\n{theater.scale}\n{theater.name}')
        elif theater == '3':
            pass
        elif theater == '4':
            pass
        elif theater == '5':
            pass
        else:
            print('다시 입력하세요')
if __name__ == '__main__':
    main()