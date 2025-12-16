# 포켓몬스터 > 몬스터들끼리 배틀 게임
# 피카츄, 이상해씨

# player_chr = "피카츄"
# player_hp = 30

# player = ["피카츄", 30, 80, 5, 77]

import random # 랜덤값을 찾아온다!!!

player = {
  "name": "피카츄",
  "hp": 30
}

enemy = {
  "name": "이상해씨",
  "hp": 30
}

# 함수 = function = 기능 = 꽃

# 함수 선언부
def attack(attacker, defender) :
  # 실행문
  damage = random.randint(5, 10)
  print(f"{attacker["name"]}의 공격!")
  print(f"{defender["name"]}에게 {damage} 데미지를 입혔습니다!")

print("==== 포켓몬 배틀 시작! ====")

while player["hp"] > 0 and enemy["hp"] > 0 :
  # 반복문의 조건식이 참인 경우, 실행될 실행구문 입력!!



# attack(player, enemy) # 함수 호출부
