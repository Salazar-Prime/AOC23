##### BEGIN BOIER CODE #####
import sys, os, re
import pandas as pd
from collections import Counter

sys.path.insert(1, "common")
from utils import *


test = False
currentDay = 7
if test:
    data = list(open(f"day{currentDay}/test.txt"))
else:
    data = list(open(f"day{currentDay}/day{currentDay}-1.txt"))
##### END BOIER CODE #####

hands = {}
for line in data:
    line = line.strip().split(" ")
    hands[line[0]] = line[1]
hands = pd.DataFrame(hands.items(), columns=["cards", "amount"])

# add two columns to hands
hands["x-kind"] = None
hands["rank"] = 0

# apply function to each row and add result to new column x-kind
hands["x-kind"] = hands.apply(
    lambda row: Counter(row["cards"]).most_common(1)[0][1], axis=1
)
# 2-pair and full house
for i in range(len(hands["x-kind"])):
    if hands["x-kind"][i] == 2:
        if Counter(hands["cards"][i]).most_common(2)[1][1] == 2:
            hands["x-kind"][i] = 2.5
    if hands["x-kind"][i] == 3:
        if Counter(hands["cards"][i]).most_common(2)[1][1] == 2:
            hands["x-kind"][i] = 3.5

# split cards into 5 columns card1, card2, card3, card4, card5
hands[["card1", "card2", "card3", "card4", "card5"]] = hands["cards"].apply(
    lambda x: pd.Series(list(x))
)
realtiveCardValue = dict(zip("23456789TJQKA", range(13)))

# convert card values to numbers
hands[["card1", "card2", "card3", "card4", "card5"]] = hands[
    ["card1", "card2", "card3", "card4", "card5"]
].replace(realtiveCardValue)

# sort in order by x-kind, card1, card2, card3, card4, card5
hands = hands.sort_values(
    by=["x-kind", "card1", "card2", "card3", "card4", "card5"], ascending=True
)

# assign rank starint from 1
hands["rank"] = range(1, len(hands) + 1)

# sum of prod of rank and amount
print(
    sum([hands["rank"][i] * int(hands["amount"][i]) for i in range(len(hands["rank"]))])
)
