from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self, n_round=1, wins=0, loses=0):
        self.round = n_round
        self.wins = 0
        self.loses = 0

    # def reset(self):
    #     self.round = 1
    #     self.wins = 0
    #     self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10. --> renamed c to consecutive_wins
        consecutive_wins = 0
        runner = cls() #define runner before running the while statement
        
        while True:
            runner.dice = Die.create_dice(5) #create dices every time you start a new run
            print("Round {}\n".format(runner.round))
            
            for die in runner.dice:
                print(die.show())
            
            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                consecutive_wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                consecutive_wins = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if consecutive_wins == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            elif prompt =='n': #added option not to play again
                break
            
            else:
                i_just_throw_an_exception()
