# 반복문 => break // continue
# break => 반복문 종료 => 빠져나온다
# continue => 컨티뉴문 다음으로 실행해야할 연산을 실행 x, 건너뛰고 반복문실행

# numbers = [14, 3, 7, 4, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# for num in numbers :
#   if num == 34 :
#     print(f"Found : {num}")
#     break
#   else :
#     print(f"Not Found : {num}")

lt = ["1", 2, 5, True, 4.3]

for item in lt :
  if type(item) is bool :
    continue
  print(type(item))