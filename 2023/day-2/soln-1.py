import re
from pathlib import Path

gameLimit = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

idPattern = re.compile(r'Game (\d+)')
colorPattern = re.compile(r'red|green|blue')
quantityPattern = re.compile(r'(\d+)')

def main() -> int:
    result = 0
    here = Path(__file__).parent

    # read file line by line
    with open(here/"input.txt") as file:
        for line in file:
            print(line)
            gameId = idPattern.search(line).group()[5:]

            if gameIsValid(line, len(gameId)):
                result += int(gameId)

        print("FINAL RESULT")
        print(result)



def gameIsValid(line: str, gameIdLength: int) -> bool:
    rounds = line[6 + gameIdLength:].split(';')
            
    for round in rounds:
        marbles = round.split(',')
        for marble in marbles:
            color = colorPattern.search(marble).group()
            quantity = int(quantityPattern.search(marble).group())
            if gameLimit[color] < quantity:
                return False

    return True
    


if __name__ == "__main__":
    main()