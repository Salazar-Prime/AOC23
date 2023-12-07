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
    # add new row to hands df
    line = line.strip().split(" ")
    hands[line[0]] = line[1]

hands = pd.DataFrame(hands.items(), columns=["cards", "amount"])
# create a new column cards-J where J is replaced with ""
hands["cards-J"] = hands["cards"].apply(lambda x: x.replace("J", ""))

# check for empty row in cards-J and set to AAAAA
for i in range(len(hands["cards-J"])):
    if hands["cards-J"][i] == "":
        hands["cards-J"][i] = "WWWWW"

# apply function to each row and add result to new column x-kind
hands["x-kind"] = hands.apply(
    lambda row: Counter(row["cards-J"]).most_common(1)[0][1], axis=1
)

# go through x-rank 2 group and check for 2- pair case
# if 2-pair case, set x-kind to 2.5
for i in range(len(hands["x-kind"])):
    try:
        secondHighest = Counter(hands["cards-J"][i]).most_common(2)[1][1]
    except IndexError:
        secondHighest = None
    if secondHighest is not None:
        if hands["x-kind"][i] == 2:
            if secondHighest == 2:
                hands["x-kind"][i] = 2.5
        if hands["x-kind"][i] == 3:
            if secondHighest == 2:
                hands["x-kind"][i] = 3.5

# count number of J's in each row
hands["J-count"] = hands["cards"].apply(lambda x: x.count("J"))

hands.loc[(hands["J-count"] == 4) & (hands["x-kind"] == 1), "x-kind"] = 5
hands.loc[(hands["J-count"] == 3) & (hands["x-kind"] == 2), "x-kind"] = 5
hands.loc[(hands["J-count"] == 3) & (hands["x-kind"] == 1), "x-kind"] = 4
hands.loc[(hands["J-count"] == 2) & (hands["x-kind"] == 3), "x-kind"] = 5
hands.loc[(hands["J-count"] == 2) & (hands["x-kind"] == 2), "x-kind"] = 4
hands.loc[(hands["J-count"] == 2) & (hands["x-kind"] == 1), "x-kind"] = 3
hands.loc[(hands["J-count"] == 1) & (hands["x-kind"] == 4), "x-kind"] = 5
hands.loc[(hands["J-count"] == 1) & (hands["x-kind"] == 3), "x-kind"] = 4
hands.loc[(hands["J-count"] == 1) & (hands["x-kind"] == 2.5), "x-kind"] = 3.5
hands.loc[(hands["J-count"] == 1) & (hands["x-kind"] == 2), "x-kind"] = 3
hands.loc[(hands["J-count"] == 1) & (hands["x-kind"] == 1), "x-kind"] = 2

# set WWWWW to JJJJJ
# hands.loc[(hands["cards-J"] == "WWWWW"), "cards-J"] = "JJJJJ"

# split cards into 5 columns card1, card2, card3, card4, card5
hands[["card1", "card2", "card3", "card4", "card5"]] = hands["cards"].apply(
    lambda x: pd.Series(list(x))
)
realtiveCardValue = dict(zip("J23456789TQKA", range(13)))
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
