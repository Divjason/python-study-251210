# 자료형
# 정수형
# 실수형
# 문자열
# 리스트
# 튜플
# 딕셔너리
# 집합 = sets

a = set()
print(type(a))

b = set([1, 2, 3, 4])
print(b)

c = {5, 6, 7, 8}
print(type(c))

# 변수 1:1
# 리스트 1:다수
# 튜플 : 리스트 내부 값이 가변적 변경 -> 고정
# 딕셔너리 : 키 : 밸류 (속성)
# 세트 : 중복값 x

d = {"A", "B", "C", "A"}
print(d)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

print(s1.issubset(s2)) # s1이 s2를 부분집합으로 가지고 있는가?