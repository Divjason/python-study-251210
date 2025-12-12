"""
1. 변수
2. 자료형 (타입확인)
3. 숫자형 (형변환)
4. 문자형
"""

# 변수이름 : 직관적 & 명시적 => 누가봐도 이 변수에는 어떤 값이 들어있을 것 같다
str1 = "I am python"
str2 = 'Python'
str3 = """How are you"""
str4 = '''Thank you'''

print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

str1_t1 = "" # 빈문자열
str2_t2 = str()

print(len(str1_t1))
print(len(str2_t2))