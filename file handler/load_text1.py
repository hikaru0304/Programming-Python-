# 원래 open()에 encoding='utf-8'을 적었었음
print('한꺼번에 전체 읽기')
f = open('text.txt', 'r')
data = f.read()
f.close()
print(data)

print('한 줄씩 읽기')
with open('text.txt', 'r') as f:
    while True:
        line = f.readline()     #line:'hello\n'
        if line == '':          #파일에서 읽어올 내용 없으면, 끝
            break
        print(line.rstrip())
print('한꺼번에 전체 읽어서, 한 줄씩 리스트')
with open('text.txt', 'r') as f:
    lines = f.readlines()
    # print(lines)
for line in lines:
    print(line.rstrip())