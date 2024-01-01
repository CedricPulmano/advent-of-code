import re
from pathlib import Path


# regex
numberPattern = re.compile(r'(\d+)')


# main runner
def main() -> int:
    here = Path(__file__).parent

    schematic = []

    # read file line by line
    with open(here/"input.txt") as file:
        for line in file:
            schematic.append(line)

    for line in schematic:
        print(line)
    sum = addPartNumbers(schematic)
    print("FINAL SUM")
    print(sum)
    

            

def addPartNumbers(schematic: [[str]]) -> int:
    sum = 0
    for row in range(len(schematic)):
        numbers = numberPattern.findall(schematic[row])
        print("NUMBERS")
        print(numbers)
        # leftBound deals with duplicate numbers on the same line
        leftBound = 0
        for number in numbers:
            top = row - 1
            left = schematic[row][leftBound:].find(number) + leftBound
            numberLength = len(str(number))
            leftBound = left + 1 + numberLength
            print("LEFT BOUND")
            print(leftBound)
            if isPartNumber(schematic, top, left, numberLength):
                print(number)
                sum += int(number)
    
    return sum


            
# checks surroundings of a number to see if it is a part number
def isPartNumber(schematic: [str], top: int, left: int, numberLength: int) -> bool:
    for r in range(top, top + 3):
        for c in range(left-1, left + numberLength + 1):
            # out of bounds
            if r < 0 or c < 0 or r >= len(schematic) or c >= len(schematic[r]):
                continue
            # not a part symbol
            if schematic[r][c] == '.' or schematic[r][c] == ' ' or schematic[r][c].isdigit() or schematic[r][c] == '\n':
                continue
            print(schematic[r][c])
            return True
    return False





# triggers main
if __name__ == "__main__":
    main()

# 413091 incorrect
# 435881 incorrect
# 442476 incorrect
# 558622 too high