# 클래스 만들어서 사용하는 이유!!
# 생성자 함수 : 클래스 안에 메뉴얼 혹은 지도 세팅할 수 있는 기반이 생성.마련
# 클래스를 선언!!

# 최초에 한 번 클래스 선언 및 생성 => 파생.상속 객체 만들고 싶어서
# 클래스 : 붕어빵 틀 -> 단팥
# 객체 = 인스턴스 객체 : 붕어빵

class Student :
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

  def study(self) :
    print(f"{self.name}이(가) 공부합니다.")
  
  def take_exam(self, subject) :
    print(f"{self.name}이(가) {subject} 시험을 봅니다.")


student1 = Student("David", 3)
student2 = Student("Jane", 2)

print(student1.name, student1.grade)
print(student2.name, student2.grade)