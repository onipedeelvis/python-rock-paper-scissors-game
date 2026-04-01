import result
import play_game

print('============= WELCOME TO ROCK-PAPER-SCISSORS GAME =============')
print('s - Scissors | p - Paper | r - Rock')

while True:
    humanChoice, computerChoice = play_game.play()

    match humanChoice:
        case 'r':
            match computerChoice:
                case 'r':
                    result.tie += 1
                    print("It is a tie!\n")
                case 'p':
                    result.computer += 1
                    print("Computer wins!\n")
                case 's':
                    result.human += 1
                    print('Human wins!\n')

        case 'p':
            match computerChoice:
                case 'p':
                    result.tie += 1
                    print("It is a tie!\n")
                case 's':
                    result.computer += 1
                    print("Computer wins!\n")
                case 'r':
                    result.human += 1
                    print('Human wins!\n')

        case 's':
            match computerChoice:
                case 's':
                    result.tie += 1
                    print("It is a tie!\n")
                case 'r':
                    result.computer += 1
                    print("Computer wins!\n")
                case 'p':
                    result.human += 1
                    print('Human wins!\n')
        



    print('============= RESULT =============')
    print(f"COMPUTER - {result.computer} | HUMAN - {result.human} | TIE - {result.tie}")
