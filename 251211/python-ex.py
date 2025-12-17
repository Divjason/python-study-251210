import random

hands = ["가위", "바위", "보"]

computer = random.choice(hands)
user = input("가위/바위/보 중 선택 : ")

print("컴퓨터 : ", computer)

if user == computer :
  print("비김!")
elif (
  (user == "가위" and computer == "보") or
  (user == "바위" and computer == "가위") or
  (user == "보" and computer == "바위")
  ) :
  print("승리!")
else :
  print("패배!")