# 11.8 심사 문제 : 리스트의 마지막 부분 삭제하기

'''
표준 입력으로 숫자 또는 문자열 여러 개가 입력되어 리스트 x에 저장됩니다.
(입력되는 숫자 또는 문자열의 개수는 정해져 있지 않음)
다음 소스 코드를 완성하여 리스트 x의 마지막 요소 5개를 삭제한 뒤 튜플로 출력되게 만드세요.


x = input().split()

________________
________________
# 입력 : 1 2 3 4 5 6 7 8 9 10
# 결과 : ('1', '2', '3', '4', '5')
'''

# 풀이
del x[-5:]
print(tuple(x))
