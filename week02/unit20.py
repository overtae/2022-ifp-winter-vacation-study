# 20.8 심사 문제 : 5아 7의 배수, 공배수 처리하기

'''
표준 입력으로 정수 두 개가 입력됩니다.
(첫 번째 입력 값의 범위는 1~1000, 두 번째 입력 값의 범위는 10~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다)
첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서 5의 배수일 때는 ‘Fizz’,
7의 배수일 때는 ‘Buzz’, 5와 7의 공배수일 때는 ‘FizzBuzz’를 출력하는 프로그램을 만드세요.
(input에서 안내 문자열은 출력하지 않아야 합니다)

# 입력 : 35 40
# 결과 : 
# FizzBuzz
# 36
# 37
# 38
# 39
# Fizz
'''

# 풀이
x, y = map(int, input().split())
for i in range(x, y + 1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
