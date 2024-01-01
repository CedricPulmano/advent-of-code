import re
from pathlib import Path

idPattern = re.compile(r'Game (\d+)')
colorPattern = re.compile(r'red|green|blue')
quantityPattern = re.compile(r'(\d+)')


# line = Game 45: 3 blue, 6 green, 1 red; 4 green, 3 blue; 8 green, 3 blue
# gameId = 45
# rounds = [' 3 blue, 6 green, 1 red', ' 4 green, 3 blue', ' 8 green, 3 blue']
# round = ' 3 blue, 6 green, 1 red'
# marbles = [' 3 blue', ' 6 green', ' 1 red']
# marble = ' 3 blue'


# main runner
def main() -> int:
    result = 0
    here = Path(__file__).parent

    # read file line by line
    with open(here/"input.txt") as file:
        for line in file:
            gameId = idPattern.search(line).group()[5:]
            rounds = line[6 + len(gameId):].split(';')
            result += minimumQuantities(rounds)

    print("FINAL RESULT")
    print(result)


# get the power of each game
def minimumQuantities(rounds: [str]) -> bool:            
    minQuantitiesRequired = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    
    # go through each round
    for round in rounds:
        marbles = round.split(',')
        for marble in marbles:
            color = colorPattern.search(marble).group()
            quantity = int(quantityPattern.search(marble).group())
            minQuantitiesRequired[color] = max(minQuantitiesRequired[color], quantity)
    
    # calculate power of set
    power = 1
    for value in minQuantitiesRequired.values():
        power *= value
    return power
    


if __name__ == "__main__":
    main()