import pygame
from keyboard import Keyboard
from display import Display

keyboard = Keyboard()
display = Display(keyboard_instance=keyboard)

def game():
    pygame.init()
    running = True
    keyboard.screen.fill('lightseagreen')
    keyboard.create_keys()
    display.get_word()
    display.create_lines()
    print(display.word_list)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for key_rect in keyboard.get_all_keys():
                    if key_rect.collidepoint(mouse_pos):
                        letter, square_rect = keyboard.get_key(mouse_pos)
                        keyboard.change_square(key_index=square_rect)
                        display.check_letter(guess=letter)
                        display.check_win()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    display.line_list = []
                    display.word_list = []
                    display.guessed_letter = []
                    display.correct_guesses = 0
                    display.wrong_guesses = 0
                    game()
# flip() the display to put your work on screen
        pygame.display.flip()

game()