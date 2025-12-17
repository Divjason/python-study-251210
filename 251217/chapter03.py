# ~인지, 아닌지? 여부 판단!!!
# 사용자로부터 어떤 값을 받았다면, 그 값이 짝수라면 ~~ 홀수라면 ~~

# if 조건문은 독립적으로 단독사용이 가능하다!
# if 조건문은 하나의 프로젝트 안에서 갯수와 무관하게 선언 및 사용가능!

if True :
  print("Good")

if False :
  print("Bad")


if False :
  print("Bad!")
else :
  print("Good!")

# 조건식
# 비교연산자

x = 10
y = 15

print(x == y) # 좌.우항 같다!!
print(x != y)
print(x >= y)
print(x <= y)

# 조건문 1) 비교연산자 2) 논리연산자

# 논리연산자 : and, or, not
# and : 좌 and 우
# or : 좌 or 우
# not : not True => False // not False => True

a = 75
b = 40
c = 50

print(a > b and b > c)
print(a > b or b > c)
print(not a > b)
print(not b > c)

score1 = 70
score2 = "A"

if score1 >= 90 or score2 == "A" :
  print("Pass")
else :
  print("Fail")