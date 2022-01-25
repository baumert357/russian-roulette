#! python3
# -*- coding: utf-8 -*-

from random import randrange
from random import sample

players = ["Spelare 1", "Spelare 2"]
trigger = "x"
round = 0
loop = True


def playerSelection():
    while True:
        howManyPlayers = input(u">>> Är ni 3 eller 4 spelare? ").lower()
        if howManyPlayers == "3":
            players.append("Spelare 3")
            break
        elif howManyPlayers == "4":
            players.append("Spelare 3")
            players.append("Spelare 4")
            break
        else:
            print(u">>> Svara '3' eller '4'.")


print(u">>> Välkommen till Rysk roulette!")

while loop:
    yourParty = input(u">>> Är ni fler än 2 spelare? ").lower()
    if yourParty == u"ja":
        loop = False
        playerSelection()
    elif yourParty == u"nej":
        loop = False
    else:
        print(u">>> Svara 'ja' eller 'nej'.")

playersLen = len(players)
for p in range(0, playersLen):
    players[p] = input(u">>> %s, vad heter du? " % players[p])
players = sample(players, playersLen)

while len(players) > 1:
    for p in players:
        round += 1
        print(u">>> Omgång:", str(round))
        print(u">>> %ss tur." % p)
        play = input(u">>> Tryck 'x'. ").lower()
        while True:
            if play == trigger:
                if randrange(0, 6) == 0:
                    print(u">>> PANG! %s dog." % p)
                    players.remove(p)
                    break
                else:
                    print(u">>> KLICK! %s överlevde." % p)
                    break
            else:
                print(u">>> Är du skraj?")
                play = input(u">>> Tryck 'x'. ").lower()

print(u">>> Vinnaren är", players[0] + "!")
