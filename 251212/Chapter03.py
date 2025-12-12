# 숫자형 연산자 : 사칙 + // + %

# 문자열 연산자
str_01 = "Python"
str_02 = "Apple"
str_03 = "How are you doing"
str_04 = "Seoul Deajeon Busan Jinju"

print(str_01 * 3)
print(str_01 + str_02) # 연결연산자
print('y' in str_01) # in 연산자
print('y' not in str_01) # not in 연산자

# 형변환
# 형태를 변환 : 1) 자동형변환 2) 명시적 형변환
# int() => 정수 형태로 바꿈
# str() => 문자열 형태로 바꿈

sample01 = 77
print(sample01, type(sample01))
print(sample01, type(str(sample01)))
print(sample01, type(int(sample01)))

# 포털사이트 > nike Nike nIke

str_05 = "python"
str_06 = "GOOGLE" # 문자열 => 각각의 문자 => 번호 (index) => 0
# 어떤 문자열이던 전체 문자열의 개수 - 1 => 마지막번째 문자의 인덱스 동일

print(str_05.capitalize())
# print(str_06.lower())

result = str_06[0].lower() + str_06[1:] # 슬라이싱 기능
# 슬라이싱 문법
# [첫번째:해당숫자 - 1]
print(result)

str_07 = "hello PYTHON"
print(str_07.swapcase())

str_08 = "hello python world"
print(str_08.title())

print(str_08.endswith("a"))
print(str_08.endswith("d"))

print(str_08.startswith("h"))
print(str_08.startswith("y")) # 주민번호 뒷자리 => 남.녀

print(str_08.replace("python", "Big"))
print(str_08.replace("\n", ""))

print(str_08.split(" ")) # 쪼개다 => 리스트 자료형

print(dir(str_08)) # __iter__ => iterable 약어

tolist = str_08.split(" ")
print(dir(tolist)) # __iter__ => iterable 약어

int01 = 7
print(dir(int01))

for i in str_08 :
  print(i)