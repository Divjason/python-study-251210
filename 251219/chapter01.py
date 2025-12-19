# for문 -> 중첩 for문
# DBMS
for i in range(2, 10) :
  for j in range(1, 10) :
    print("{:4d}".format(i * j), end="") # \n
  print()