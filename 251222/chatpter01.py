# 함수 : 값을 받아서 내부 실행문을 통해서 연산처리 후 값을 반환할 수 있도록 해주는 기능

def first_func(w) :
  a = f"Hello, {w}"
  return a

b = first_func("world")

print(b)

# 함수의 매개변수로 "튜플"
def args_func(*args) :
  for i, v in enumerate(args) :
    print("Result : {}".format(i), v)
  print("----")

args_func("park", "kim")

# 함수의 매개변수로 딕셔너리값을 받는 경우!!
def dict_func(**dargs) :
  for v in dargs.keys() :
    print("{} :".format(v), dargs[v])
  print("----")

dict_func(name = "park", age = 20, address = "seoul")

# dict_test = {
#   "name": "David"
# }