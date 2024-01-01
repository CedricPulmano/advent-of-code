import re
from pathlib import Path

# main runner
def main() -> int:
    here = Path(__file__).parent

    # read file line by line
    with open(here/"input.txt") as file:
        for line in file:
            print(line)
    

# triggers main
if __name__ == "__main__":
    main()
