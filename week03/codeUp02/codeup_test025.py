# 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

# 입력 :
# 75254

# 출력 :
# [70000]
# [5000]
# [200]
# [50]
# [4]
num = str(input())
#i = 4
i = len(num) - 1
for j in num:
    print("[{}{}]".format(j, '0'*i))
    i = i - 1
