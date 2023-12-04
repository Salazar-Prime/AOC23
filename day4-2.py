import re, math

data = list(open("inputs/day4-1.txt"))
data = [x.strip().split(": ") for x in data]

cardSum = 0
scoreBoard = [1 for _ in range(len(data))]

for idx, card in enumerate(data):
    # get card number card <card number> with regex
    cardNo = re.search(r"\d+", card[0]).group()
    winNo, myNo = card[1].split("|")
    winNo, myNo = winNo.split(), myNo.split()

    # get number of matches in myNo with winNo
    matches = len(set(winNo) & set(myNo))
    if matches > 0:
        cardSum += 2 ** (matches - 1)

    for i in range(matches):
        scoreBoard[idx + i + 1] += scoreBoard[idx]

print(sum(scoreBoard))
