# ◼ 평균 점수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다)
# . 단, 평균 점수를 출력할 때는 소수점 이하 자리는 버립니다
# (정수로 출력).
# 입력 : 83 92 87 90
# 결과 : 88

a, b, c, d = map(int, input().split())
print((a+b+c+d)//4)