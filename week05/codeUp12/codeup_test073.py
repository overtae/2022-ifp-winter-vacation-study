#정수가 순서대로 입력된다.
#(단, 개수는 알 수 없다.)

#0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

#입력
#정수가 순서대로 입력된다.
# 출력
# 입력된 정수를 줄을 바꿔 하나씩 출력하는데, 
# 0이 입력되면 종료한다. (0은 출력하지 않는다.)
number = list(map(int, input().split()))

for i in number:
    if i == 0:
        break
    else:
        print(i)
