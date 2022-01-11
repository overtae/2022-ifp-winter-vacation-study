# 표준 입력으로 정수가 입력됩니다. 
# 입력된 정수의 구구단을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 출력 형식은 숫자 * 숫자 = 숫자처럼 만들고 숫자와 *, = 사이는 공백을 한 칸 띄웁니다.
# ex)
# >>> 2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# >>> 7
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# 7 * 4 = 28
# 7 * 5 = 35
# 7 * 6 = 42
# 7 * 7 = 49
# 7 * 8 = 56
# 7 * 9 = 63
# 문제 제출 코딩도장 Python
# 답안 제출 2022/01/11 15:51 경준현

dan = int(input())
for i in range(1,10):
    print(dan , "*" , i , "=" , dan*i)

# 표준입력으로 확인하고싶은 단을 입력받는다, 정수로 입력받아야 하므로 int로 캐스팅하였다.
# for 문의 range를 이용하여 9번 반복한다. 1, 10이므로 1~9까지이다.