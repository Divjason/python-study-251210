# 크롤링 > 리스트!!

a = [] # 리스트 선언!!! -> 비어있는 리스트 // 값을 할당 x
a.append(1)

b = list()

c = [70, 75, 80, 85] # 리스트 선언 & 값을 할당

d = [100, 1000, "Ace", "Base", "Cap"] # 기존 변수의 형태들은 1:1 구조
# 변수 1개에 값 1개
# 100개 => 100개 변수

print(type(a))
print(a)
print(type(b))
print(type(c))
print(c)
print(type(d))
print(d)

# 리스트 라는 자료구조 > 다양한 속성 및 메서드 함수 및 기타 내장 함수
# 리스트 안에 입력된 값의 갯수 파악 => len()

# 리스트 역시 연산가능!!!

str1 = "안"
str2 = "녕"

result = str1 + str2 # 문자열도 연산이 가능, 단, + : 연결연산자
print(result)

print(len(d))

print(c + d) # 리스트도 연산이 가능, 단, + : 연결연산자

# 리스트 자료형 => 리스트 안에 담겨있는 값들이 고유한 순번을 가지고 있음
# 인덱스 (index)
# 컴퓨터 2진수 (0, 1)

print(c[0] - c[1]) # 리스트 자료형에 입력된 값을 고유한 자료형을 그대로 유지!!!

e = [1, 2, [3, 4, 5]] # 중첩 리스트

print(e[0] + e[2][0])

# 리스트, 문자열 유사함 -> iter -> 슬라이싱
print(e[1] * e[2][-2])

f = "base"
f_list = list(f)
print(f_list)

print(c * 3) # 리스트 자료형 +, *

print(type(str(c[2])))