# 변수 & 자료형 & 자료타입 확인

# 문자열 VS 문자
str1 = "Python" # str1변수를 선언하고, "Python" 문자열을 할당했다
str2 = "7" # crawling => 무신사, 올리브영, 인스타그램
# 인스타그램 > 올리브영 > 100개 > 좋아요 갯수 평균

# 숫자 (정수)
int1 = 7 # interger
# 정수 => bigint / longint

# 논리형
bool1 = True # Boolean => False

# 실수
float1 = 3.14

# 리스트
list1 = [str1, int1] # [자녀의 나이 : 3, 오늘 간식 : 5, 108, 220, 7]

# 딕셔너리
dict1 = {
  "name": "David"
}

# 튜플
tuple1 = (int1, float1)

# 세트 = 집합
set1 = {bool1, str1}
# 인스타그램 > 피드 > 문서함
# A 피드 > 문서함

# 외부에서 데이터를 수집해서 가져오는 경우!
# 어떤 데이터를 최초에 작성 X

# 데이터 타입 확인.출력

print(type(str1)) # 내장함수 -> 인수 | 인자값
# python => oop => Oriented Object Programming 언어

# string = 문자열

print(type(str1))
print(type(bool1))
print(type(int1))
print(type(float1))
print(type(dict1))
print(type(list1))
print(type(tuple1))