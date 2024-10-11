from pygame import mixer
import pygame


class Sounds:
    def __init__(self):
        mixer.init()

        self.destroySound = pygame.mixer.Sound("assets/pickupCoin.wav")

        self.sounds = [
            pygame.mixer.Sound("assets/Untitled.wav"),
            pygame.mixer.Sound("assets/Untitled (1).wav"),
            pygame.mixer.Sound("assets/Untitled (2).wav"),
            pygame.mixer.Sound("assets/Untitled (3).wav"),
            pygame.mixer.Sound("assets/Untitled (4).wav"),
            pygame.mixer.Sound("assets/Untitled (5).wav"),
            pygame.mixer.Sound("assets/Untitled (6).wav"),
            pygame.mixer.Sound("assets/Untitled (7).wav"),
            pygame.mixer.Sound("assets/Untitled (8).wav"),
            pygame.mixer.Sound("assets/Untitled (9).wav"),
            pygame.mixer.Sound("assets/Untitled (10).wav"),
            pygame.mixer.Sound("assets/Untitled (11).wav"),
        ]
        self.i = 0

    def play(self):
        # stop all sound
        for sound in self.sounds:
            sound.stop()

        # play sound
        sound = self.sounds[self.i]
        sound.play()
        self.i += 1
        if self.i >= len(self.sounds):
            self.i = 0

    def playDestroySound(self):
        self.destroySound.play()

sounds = Sounds()
