import re
from pathlib import Path

# main runner
def main() -> int:
    here = Path(__file__).parent

    totalPoints = 0

    # read file line by line
    with open(here/"input.txt") as file:
        for line in file:
            strippedLine = line.strip()
            totalPoints += scorePointsOfCard(strippedLine[strippedLine.index(':') + 1:])

    print("TOTAL POINTS")
    print(totalPoints)
            

# returns points of card
def scorePointsOfCard(line: str) -> int:
    points = 0
    items = line.split(" ")
    winningNumbers = {}
    isWinningNumber = True
    for item in items:
        # empty character; can ignore
        if item == '':
            continue
        # | character, stop counting winning numbers
        if item == '|':
            isWinningNumber = False
            continue
        # add to winning numbers dictionary
        if isWinningNumber:
            winningNumbers[item] = winningNumbers.get(item, 0) + 1
        else:
            # reduce count in dictionary if it is included; else ignore
            if winningNumbers.get(item) and winningNumbers.get(item) > 0:
                winningNumbers[item] -= 1
                points = 1 if points == 0 else points * 2
    return points
    


# triggers main
if __name__ == "__main__":
    main()


# 20009 too low
