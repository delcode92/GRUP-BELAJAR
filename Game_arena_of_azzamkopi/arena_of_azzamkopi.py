import random
import time


hero1 = {
  "namaplayer": "Buggy
  "role": "carry",
  "darah": 1000,
  "attackDamage": 25,
} 

hero2 = {
  "namaplayer": "ryokugyu",
  "role": "carry",
  "darah": 1000,
  "attackDamage": 25,
} 

hero3 = {
  "namaplayer": "kurohige",
  "role": "carry",
  "darah": 1000,
  "attackDamage": 25,
} 

namaplayer= [hero1["namaplayer"], hero3["namaplayer"], hero2["namaplayer"]]
dmgplayer= [hero1["attackDamage"], hero3["attackDamage"], hero2["attackDamage"]]
darahplayer= [hero1["darah"], hero3["darah"], hero2["darah"]]


def duel():
    kemampuanpukul = random.randint(20,53)
    korban = namaplayer[random.randint(0, 2)]
    pelaku = namaplayer[random.randint(0, 2)]
    kondisi1 = ( ( dmgplayer[random.randint(0, 2)] * kemampuanpukul ) )
    sisadarah = darahplayer[random.randint(0, 2)] - kondisi1

    if korban == pelaku:
      print("player", pelaku, "menang WO")      
    else:
      print("player", pelaku,"memukul", korban, "dengan damage", kondisi1)
      print("sisa darah player", namaplayer[random.randint(0, 2)], "adalah", sisadarah)

jumlahronde = 5
for i in range(jumlahronde):
    print("ronde ", i+1 )
    duel()
    print(" ")
    time.sleep(2)
