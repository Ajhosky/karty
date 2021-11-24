import random
gracz1 = []
gracz2 = []
gracz3 = []
gracz4 = []
color = ["diamond","heart","club","spade"]
ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
deck = []
gracze = [gracz1,gracz2,gracz3,gracz4]
num_players = 4
num_cards = 5

for rank in range(13):
         for colors in range(4):
            deck.append(f"{ranks[rank]} {color[colors]}")

random.shuffle(deck)
for card in range(num_cards):
    for player in range(num_players):
       gracze[player].append(deck.pop(0))


print(f"karty gracza 1: {gracz1}") 
print(f"karty gracza 2: {gracz2}") 
print(" ")
print("---------------------------------------------------")
print(" ")
# print(f"karty gracza 3: {gracz3}") 
# print(f"karty gracza 4: {gracz4}") 

cardsplayer1 = 0
cardsplayer2 = 0
def porownaj(cardsplayer1, cardsplayer2):
   for x in range(num_cards):
      splitkarta1 = gracz1.pop(0)   #splitkarta to zmienna pomocnicza. karta gracza 1 podzielona splitem, by wziac tylko range tej karte bez color
      cardsplayer1 = ranks.index(splitkarta1.split()[0])   #przypisuje wartosc po indexie rangi
      splitkarta2 = gracz2.pop(0)
      cardsplayer2 = ranks.index(splitkarta2.split()[0])
      if(cardsplayer1>cardsplayer2):
       print(f"({x+1} kolejka: karta {splitkarta1} jest wieksza od {splitkarta2})")
      else:
       print(f"({x+1} kolejka: karta {splitkarta1} jest mniejsza od {splitkarta2}")
   if(cardsplayer1 == cardsplayer2):
      print(f"({x+1} kolejka: karta {splitkarta2} jest równa {splitkarta1}")


porownaj(cardsplayer1,cardsplayer2)






