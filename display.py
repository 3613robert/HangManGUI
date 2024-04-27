import pandas as pd
import random
import pygame

class Display:
    def __init__(self, keyboard_instance):
        self.keyboard_instance = keyboard_instance
        self.line_list = []
        self.word_list = []
        self.guessed_letter = []
        self.correct_guesses = 0
        self.wrong_guesses = 0
        self.hangman_images = [pygame.image.load('images/hangman0.png'),
                               pygame.image.load('images/hangman1.png'),
                               pygame.image.load('images/hangman2.png'),
                               pygame.image.load('images/hangman3.png'),
                               pygame.image.load('images/hangman4.png'),
                               pygame.image.load('images/hangman5.png'),
                               pygame.image.load('images/hangman6.png'),
                               pygame.image.load('images/hangman7.png')]
        self.score = 0
        self.highscore = 0

    def get_word(self):
        data = pd.read_csv('words.csv', header=None)
        words_row = data.iloc[1]
        chosen_word = random.choice(words_row)
        for letter in chosen_word[1:]:
            self.word_list.append(letter)
        return chosen_word

    def create_lines(self):
        for i in range(len(self.word_list)):
            lines = pygame.draw.line(self.keyboard_instance.screen,
                                     'black',
                                     (30 + i * 30, 305),
                                     (50 + i * 30, 305), )
            self.line_list.append(lines)

    def check_letter(self, guess):
        if guess in self.guessed_letter:
            pass
        else:
            self.guessed_letter.append(guess)
            found_letter = False
            for i, letter in enumerate(self.word_list):
                if guess.lower() == letter:
                    text_font = pygame.font.SysFont("Courier", 48, bold=True)
                    rendered_letter = text_font.render(guess, False, 'black')
                    letter_x = self.line_list[i].left + (self.line_list[i].width - rendered_letter.get_width()) / 2
                    letter_y = self.line_list[i].top - rendered_letter.get_height()  # Place above the line
                    self.keyboard_instance.screen.blit(rendered_letter, (letter_x, letter_y))
                    self.correct_guesses += 1
                    found_letter = True
            if not found_letter:
                self.guessed_wrong()
                self.display_hangman()

    def guessed_wrong(self):
        self.wrong_guesses += 1

    def display_hangman(self):
        if self.wrong_guesses < len(self.hangman_images)-1:
            # Blit the corresponding hangman image onto the screen
            self.keyboard_instance.screen.blit(self.hangman_images[self.wrong_guesses], (475, 20))
        else:
            self.keyboard_instance.screen.blit(self.hangman_images[self.wrong_guesses], (475, 20))
            # Display a message when the hangman is fully revealed
            font = pygame.font.SysFont("Courier", 60, bold=True)
            continue_font = pygame.font.SysFont("Courier", 36, bold=True)
            text = font.render("Game Over!", True, (255, 0, 0))
            continue_text = continue_font.render("Press y to play again", True, 'red')
            self.keyboard_instance.screen.blit(text, (100, 175))
            self.keyboard_instance.screen.blit(continue_text, (60, 75))
            self.score = 0

    def check_win(self):
        if self.correct_guesses == len(self.word_list):
            font = pygame.font.SysFont("Courier", 60, bold=True)
            continue_font = pygame.font.SysFont("Courier", 36, bold=True)
            text = font.render("You've won!", True, 'lightskyblue1')
            continue_text = continue_font.render("Press y to play again", True, 'lightskyblue1')
            self.keyboard_instance.screen.blit(text, (100, 175))
            self.keyboard_instance.screen.blit(continue_text, (60, 75))
            return True

    def display_score(self):
        font = pygame.font.SysFont("Courier", 24, bold=True)
        score_text = font.render(f'Score:{self.score}', True, 'lightskyblue2')
        self.keyboard_instance.screen.blit(score_text, (10, 25))

    def display_highscore(self):
        with open('highscore.txt', 'r') as data:
            highscore = data.read()
            self.highscore = int(highscore)
        if self.score > self.highscore:
            with open('highscore.txt', 'w') as data:
                data.write(str(self.score))
        font = pygame.font.SysFont("Courier", 24, bold=True)
        highscore_text = font.render(f'Highscore:{self.highscore}', True, 'lightskyblue2')
        self.keyboard_instance.screen.blit(highscore_text, (10, 50))