# 함수 = 프로그래밍 언어 꽃
# function = 기능
# 자주 & 반복적으로 실행하고자 하는 기능들을 정의!!!
# 필요할 때마다 가져다 사용할 수 있도록

# 선언 & 호출
# 인자값 | 인수 (옵션)
# 선언하는 단계에서 매개변수

# 함수 선언!
def function1() :
  print("함수 호출", 2 * 4)

# 함수 호출!
function1()

# 파이썬 => 객체지향 프로그래밍 OOP 언어
# Class => 속성, 객체, 함수

def function2(a, b) :
  print(f"호출 {a} * {b} = {a * b}")

function2(2, 4)
function2(10, 10)

# abc = 

# 함수는 선언단계에서 함수를 호출할 때에 값을 반환시킬 수도 있고, 그렇지 않을 수도 있음

def return_fnc(w1) :
  value = f"Hello {str(w1)}"
  return value


a = return_fnc("World")

print(a)

# 다중반환

def func_mul(x) :
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return y1, y2, y3

func_re = func_mul(10)

# print(type(func_re))

# for item in func_re :
#   print(item)

# print(func_re[0])

x, y, z = func_mul(10) # 구조분해할당

print(x, y, z)