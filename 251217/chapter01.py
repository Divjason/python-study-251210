# 딕셔너리
# a = []
# b = ()
# c = {} | set

a = {
  "name": "kim",
  "name": "lee"
}

b = {
  "arr": [1, 2, 3, 4]
}

c = {
  "Age": 20,
  "Name": "David"
}

# d = list()
# d.append()

# d = [1, 2, 3]

e = dict([
  ("Name", "Park"),
  ("City", "Seoul")
])

print(type(e))

# 대괄호 표기법을 통해서 딕셔너리 안에 있는 값을 찾아올 수 있음!

print(c["Age"]) # 대괄호 표기법
print(c.get("Name")) # get 메서드 함수 사용법

c["Address"] = "Seoul"

print(c)

# print(dir(c))

# print(len(c))

for item in c :
  print(item)

# c[0] # dir(개체명) => 속성 확인!! __iter__ : iterable
# 반복순회할 수 있는 속성을 가지고 있는 것이다!!
# 순번 : 문자열, 리스트 => index

# __iter__ -> index

print(c.keys())
print(c.values())
print(c.items())

print(dir(c))

print(c)

c.pop("Name") # 리스트 아이템 제거

print(c)

print(c.popitem())
print(c)

f = {
  "title": "Python",
  "price": 38000,
  "publisher": "sbs아카데미"
}

print(type(f))
print("price" in f)