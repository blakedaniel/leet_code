class Hangman():
    def __init__(self, word:str='default', guesses:int=10):
        self.word = list(word)
        self.num_guess = guesses
        self.rem_chars = [chr(num) for num in range(97,97+26)]
        self.guessed = ['_' for char in word]
        
    def display(self):
        print('REMAINING GUESSES:', self.num_guess)
        print('REMAINING LETTERS\n',' '.join(self.rem_chars))
        print('YOUR WORD:\n',''.join(self.guessed))
        print('~'* 50)
        
    def guess(self, string:str):
        if len(string) != 1:
            string = list(string)
            if self.word != string:
                return False
            self.guessed = string
            return True
        
        self.rem_chars.remove(string)
        for idx, char in enumerate(self.word):
            if char == string:
                self.guessed[idx] = string
        return string in self.word
        
    def update_num(self):
        self.num_guess -= 1
    
def main():
    word = input("What's the word? ")
    hangman = Hangman(word, 10)
    while hangman.num_guess > 0 and hangman.word != hangman.guessed:
        hangman.display()
        string = input("What's your guess? ")
        correct = hangman.guess(string)
        if not correct:
            hangman.update_num()
    if hangman.num_guess != 0:
        print('CONGRATS!! YOU WIN!!')
    else:
        print('Better luck next time')

main()