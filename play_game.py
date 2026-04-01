import random, result

def play() -> tuple[str, str]:
    humanChoice: str|None = None

    while humanChoice not in result.choices:
        humanChoice = input(f"\nEnter your choice{' again' if humanChoice is not None else ''}:\n> ")

        if humanChoice in result.choices:
            print(f"You choose {result.choices[humanChoice]}\n")
        else:
            print("You should input either 'r', 'p', or 's'\n")

    computerChoice = random.choice(['r', 'p', 's'])

    print(f"Computer chooses: {result.choices[computerChoice]}\n")

    return humanChoice, computerChoice
