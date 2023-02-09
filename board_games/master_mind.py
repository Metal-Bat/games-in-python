import random

# Red, Green, Blue, Yellow, Grey, White
COLORS = ["R", "G", "B", "Y", "G", "W"]
TRIES = 10
CODE_LENGTH = 4


class MasterMind:
    """Master Mind game was invented in 1972
    Original game has 6 color and 4 combinations but in this code you can easily
    change rules and add your own color, combination or tries
    """

    def __init__(self) -> None:
        game_starts = input("Do you want to play Master Mind? y/n\n").lower()
        if game_starts == "y":
            print(f"Solve it if you dare in {TRIES} tries!!!")
            print("Your answers should be in this format", *COLORS)

            code = self.generate_code()
            for attempts in range(1, TRIES + 1):
                guess = self.guess_code(attempts)
                correct_pos, incorrect_pos = self.check_code(guess=guess, real_code=code)

                if correct_pos == CODE_LENGTH:
                    print(f"YOU guessed it in {attempts} attempts")
                    break
                print(f"your correct positions are {correct_pos}\nyour Incorrect Positions are {incorrect_pos}")
            else:
                print("loser color order was :", *code)

    def generate_code(self) -> list[str]:
        """generates a color code combination

        Args:
            self (obj)

        Returns:
            list[str]: this list is made random base on number of combinations
        """
        return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

    def guess_code(self, attempts: int) -> list[str]:
        """get user code and makes sure the code is in correct format

        Args:
            self (obj)
            attempts (int): how many times user tried to guess

        Returns:
            list[str]: list of user colors to guess
        """
        while True:
            guess = input(f"your {attempts} attempt Guess: ").upper().split(" ")
            if len(guess) != CODE_LENGTH:
                print(f"You must guess {CODE_LENGTH} colors")
                continue

            for color in guess:
                if color not in COLORS:
                    print(f"Invalid color: {color}. Try again.")
                    break
            else:
                break
        return guess

    def check_code(self, guess: list[str], real_code: list[str]) -> tuple(int):
        """_summary_

        Args:
            self (obj)
            guess (list[str]): list of user guessed color
            real_code (list[str]): list of real code color

        Returns:
            tuple(int): correct_pos and incorrect_pos
        """
        color_counts = {}
        correct_pos = 0
        incorrect_pos = 0

        for color in real_code:
            if color not in color_counts:
                color_counts[color] = 0
            color_counts[color] += 1

        for guess_color, real_color in zip(guess, real_code):
            if guess_color == real_color:
                correct_pos += 1
                color_counts[guess_color] -= 1

        for guess_color, real_color in zip(guess, real_code):
            if guess_color in color_counts and color_counts[guess_color] > 0:
                incorrect_pos += 1
                color_counts[guess_color] -= 1

        return correct_pos, incorrect_pos


if __name__ == "__main__":

    MasterMind()
