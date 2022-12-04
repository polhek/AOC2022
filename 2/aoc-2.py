from pathlib import Path

""" 
    A == X == ROCK == 1 
    B == Y == PAPER == 2
    C == Z == SCISSORS == 3
    -------------
    X = LOSE
    Y = DRAW
    Z = WIN
    -------------
    LOSE = 0
    DRAW = 3 
    WIN = 6
"""

myScore = int(0)
p = Path(__file__).with_name("input.txt")


def check_score(elfPick: str, matchOutcome: str) -> int:
    roundScore = int(0)
    myPick = ""

    if matchOutcome == "X":
        roundScore += 0
    if matchOutcome == "Y":
        roundScore += 3
    if matchOutcome == "Z":
        roundScore += 6

    if matchOutcome == "Y":
        myPick = elfPick

    if matchOutcome == "X":
        if elfPick == "A":
            myPick = "C"
        if elfPick == "B":
            myPick = "A"
        if elfPick == "C":
            myPick = "B"

    if matchOutcome == "Z":
        if elfPick == "A":
            myPick = "B"
        if elfPick == "B":
            myPick = "C"
        if elfPick == "C":
            myPick = "A"

    if myPick == "A":
        roundScore += 1
    if myPick == "B":
        roundScore += 2
    if myPick == "C":
        roundScore += 3
    return roundScore


with p.open("r") as plays:
    lines = plays.readlines()
    for line in lines:
        splitText = line.split()
        elfPick = splitText[0]
        myPick = splitText[1]
        myScore += check_score(elfPick, myPick)

print(myScore)
