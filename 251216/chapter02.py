# 각각의 프로그래밍 언어 문법 많음!!
# 문법 > 프로그램 x (10년차 프로그래머 학습량 == 8년차 전공의)
# CRUD 문법 순서 학습 (추천)
# Create
# Read
# Update (수정, 편집)
# Delete

# 리스트 자료형(구조) 값을 추가하는 방법

city = ["서울시"]
city_plus = ["부산", "대구"]

city.append("부산시") # "메서드" 함수 => 리스트 뒤에서부터 값
city.insert(0, "강원도")
city.extend(["수원시", "용인시"]) # 한번에 여러개의 값을 넣고싶을 때

print(city + city_plus) # 함수

city.pop() # 인자값이 존재하지 않으면 뒤에서 값을 제거
city.pop(0)

city.remove("부산시")

del city[1]

print(city)

# 리스트 B > AAA 형태
# > U / D
# 자전거

