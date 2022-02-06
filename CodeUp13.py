# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자

num = int(input())

print('== #1 ==')

answer = 0
for i in range(2, num+1, 2):
  answer += i
print(answer)

print('== #2 ==')

# 원하는 문자가 입력될 때까지 반복 출력하기
# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자

word = input().split()

print('== #1 ==')
#1
for w in word:
  print(w)
  if w == 'q': break

print('== #2 ==')
#2
i = 0
while word[i] != 'q':
  print(word[i])
  i += 1
print(word[i])

# 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지 계속 더하는 프로그램을 작성해보자
# 즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다

end_point = int(input())

print('== #1 ==')
#1
total = 0
i = 0
while total < end_point:
  i += 1
  total += i
print( i )

print('== #2 ==')

# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자

n, m = map(int, input().split())

for n in range(1, n+1):
  for m in range(1, m+1):
    print(n, m)

# 6진수 구구단
# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운 영일(01)이는 16진수끼리 곱하는 16진수 구구단에 대해서 궁금해졌다
# A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자
# (단, A ~ F 까지만 입력된다)

char = input()

for i in range(1, 16):
  print( '%s*%s=%s' %(char, hex(i)[2:].upper(), hex(int(char, 16) * i)[2:].upper()) )

# 3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다
# 3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자

num = int(input())

print('== #1 정답 ==')
#1
for i in range(1, num+1):
  count = i if i%3 else 'X'
  print(count, end=' ')

print('\n== #2 오답 ==')
#2
for i in range(1, num+1):
  count = 'X' if '3' in str(i) or '6' in str(i) or '9' in str(i) else i
  print(count, end=' ')

# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 빛의 색을 만들어 내려고 한다
# 빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때,
# (빛의 강약에 따라 0 ~ n-1 까지 n가지의 빛 색깔을 만들 수 있다)
# 주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과 총 가짓 수를 계산해보자

r, g, b = map(int, input().split())

count = 0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i, j, k)
      count += 1
print(count)

# 1초 동안 마이크로 소리강약을 체크하는 수를 h (헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다)
# 한 번 체크한 결과를 저장하는 비트 b (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)
# 좌우 등 소리를 저장할 트랙 개수인 채널 c (모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다)
# 녹음할 시간 s가 주어질 때, 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

h, b, c, s = map(int, input().split())

result = h*b*c*s
resultMB = result / (8 * 1024**2)
print(round(resultMB, 1), 'MB')

# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때, 압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자

w, h, b = map(int, input().split())
result = (w*h*b) / (8 * 1024**2)
print( round(result, 2), 'MB' )

# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자
# 즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다
# 하지만, 이번에는 그 때의 합을 출력해야 한다
# 예를 들어 57을 입력하면 1+2+3+...+8+9+10=55에 다시 11을 더해 66이 될 때, 그 값 66이 출력되어야 한다

end_point = int(input())
total = 0
i = 1
while total < end_point:
  total += i
  i += 1
print( total )

# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자
# 예를 들면, 1 2 4 5 7 8 10 11 13 14 ... 와 같이 출력하는 것이다

num = int(input())

for i in range(1, num+1):
  if i%3:
    print(i, end=' ')

# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(series)이라고 한다
# 예를 들어 1 4 7 10 13 16 19 22 25 ... 은 1부터 시작해 이전에 만든 수에 3을 더해 다음 수를 만든 수열이다
# 이러한 것을 수학에서는 앞뒤 수들의 차이가 같다고 하여 등차(차이가 같다의 한문 말) 수열이라고 한다
# 수열을 알게 된 영일이는 갑자기 궁금해졌다
# "그럼.... 123번째 나오는 수는 뭘까?"
# 영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다
# 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자

a, d, n = map(int, input().split())

i = a
count = 0
arith = []
while count < n:
  arith.append(i)
  i += d
  count += 1
print( arith[-1] )

# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열이라고 한다
# 예를 들어 2 6 18 54 162 486 ... 은 2부터 시작해 이전에 만든 수에 3을 곱해 다음 수를 만든 수열이다
# 이러한 것을 수학에서는 앞뒤 수들의 비율이 같다고 하여 등비(비율이 같다의 한문 말) 수열이라고 한다
# 등비 수열을 알게된 영일이는 갑자기 궁금해졌다
# "그럼.... 13번째 나오는 수는 뭘까?"
# 영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다
# 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자

a, r, n = map(int, input().split())

i = a
count = 0
geom = []
while count < n:
  geom.append(i)
  i *= r
  count += 1
print( geom[-1] )

# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열이라고 한다
# 예를 들어 1 -1 3 -5 11 -21 43 ... 은 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다
# 이런 이상한 수열을 알게 된 영일이는 또 궁금해졌다
# "그럼.... 13번째 나오는 수는 뭘까?"
# 영일이는 물론 수학을 아주 잘하지만 이런 문제는 본 적이 거의 없었다...
# 그래서 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램을 만들어보자

a, m, d, n = map(int, input().split())

i = a
prog = []
while len(prog) < n:
  prog.append(i)
  i = i*m+d
print( prog[-1] )

# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
# 예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다

a, b, c = map(int, input().split())
day = 1
while day%a != 0 or day%b != 0 or day%c != 0:
  day += 1
print( day )

day = 1
while 1:
  day += 1
  if day%a == 0 and day%b == 0 and day%c == 0: break
print( day )