# 자료형 -> 숫자형 자료 -> 연산자!!
"""
+
-
*
/

// : 몫
% : 나머지 -> 짝수, 홀수 
"""

i1 = 39
i2 = 939
i3 = 7
i4 = 3
i5 = 3.0
big_int1 = 829034802938948205809
big_int2 = 128738912739812712345
f1 = 1.234
f2 = 3.939
# s1 = "10"
# total = i1 + s1
# print(total)

print(">>>")
print("39 + 939 =", i1 + i2) # 가운데 + : 연산자, 피연산자
print(f"{i1} + {i2} = {i1 + i2}") # f-string 문법 : formatted String

print(f"{i3} // {i4} = {i3 // i4}")
print(f"{i3} % {i4} = {i3 % i4}")

print(f"{i3} // {i5} = {i3 // i5}")
print(f"{i3} % {i5} = {i3 % i5}")

# 자동 형변환 : 어떤 상이한 형태의 자료가 연산처리되었을 때, 자동으로 형변환
# 수동(명시적) 형변환 :
i7 = 7
i8 = "8"
b7 = True

print(type(i8))
print(type(int(i8)))
print(int(False)) # 2진수 : 0, 1 => 비트 => 바이트 => 16진수 / 8진수
# 0 : false, 1 : true