# a = {
#   "name": "david",
#   "age": 20
# }

# s = set()

# for item in a :
#   s.add(a[item])


# print(s)

# 반복문!!!
# 어떤 연산 처리를 한치의 오차도 없이 빠른속도로 무한 반복할 수 있는 능력
# __iter__ 

# a = [1, 2, 3, 4]

# for index in a :
#   print(index)

# for v1 in range(10) :
#   print(v1 + 1)

# for v2 in range(1, 11) :
#   print(v2)

# for v3 in range(1, 10, 2) :
#   print(v3)

# 사칙연산자
# 비교연산자
# 논리연산자

# if 조건문 : 비교연산자, 논리연산자
# for 문 : 복합대입연산자

# b = 0

# b = b + 1 # 코드가 반복적으로 x
# b += 1

# b -= 1
# b *= 1
# b /= 1
# b %= 1

# sum = 0

# for v in range(1, 11) :
#   sum += v

# print(sum)

# print(type(range(1, 11)))

# print(sum(range(1, 11, 2)))

# names = ["kim", "lee", "park", "choi"]

# for index, name in enumerate(names) :
#   print(f"{index + 1}. {name}")

s = "Beautiful"

# print(dir(s))

# for item in s :
#   print(item)

a = {
  "name": "David",
  "age": 20
}

# print(dir(a))

for item in a :
  print(item)
  print(f"{item} = {a[item]}")

name = "FineAppLE"

# print(dir(name))

for n in name :
  if n.isupper() :
    print(n)
  else :
    print(n.upper())