import random

hands = ["가위", "바위", "보"]

computer = random.choice(hands)
user = input("가위/바위/보 중 선택 : ")

print(user, computer)