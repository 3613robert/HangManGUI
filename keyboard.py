import pygame

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]


class Keyboard:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 500))
        self.key_rects = []

    def create_keys(self):
        for i in range(0, 9):
            pygame.Surface.fill(self.screen, 'lightskyblue1', ((40 + (58 * i), 355), (48, 30)))
            upper_row = pygame.draw.rect(self.screen, 'cyan4', ((40 + (58 * i), 355), (48, 30)), 2)
            self.key_rects.append(upper_row)
            text_font = pygame.font.SysFont("Courier", 24, bold=True)
            letter = text_font.render(ALPHABET[i], False, 'lightgoldenrod4')
            self.screen.blit(letter, (54 + (58 * i), 355))
        for i in range(0, 8):
            pygame.Surface.fill(self.screen, 'lightskyblue1', ((65 + (58 * i), 405), (48, 30)))
            middle_row = pygame.draw.rect(self.screen, 'cyan4', ((65 + (58 * i), 405), (48, 30)), 2)
            self.key_rects.append(middle_row)
            text_font = pygame.font.SysFont("Courier", 24, bold=True)
            letter = text_font.render(ALPHABET[i + 9], False, 'lightgoldenrod4')
            self.screen.blit(letter, (79 + (58 * i), 405))
        for i in range(0, 9):
            pygame.Surface.fill(self.screen, 'lightskyblue1', ((40 + (58 * i), 455), (48, 30)))
            bottom_row = pygame.draw.rect(self.screen, 'cyan4', ((40 + (58 * i), 455), (48, 30)), 2)
            self.key_rects.append(bottom_row)
            text_font = pygame.font.SysFont("Courier", 24, bold=True)
            letter = text_font.render(ALPHABET[i + 17], False, 'lightgoldenrod4')
            self.screen.blit(letter, (54 + (58 * i), 455))

    def get_all_keys(self):
        return self.key_rects

    def get_key(self, mouse_pos):
        for rect_index, rect in enumerate(self.key_rects):
            if rect.collidepoint(mouse_pos):
                return ALPHABET[rect_index], rect_index
        return None  # Return None if no key is clicked

    def change_square(self, key_index):
        pygame.Surface.fill(self.screen, 'black', self.key_rects[key_index])
        pygame.draw.rect(self.screen, 'black', self.key_rects[key_index])
