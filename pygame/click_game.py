import time

spiderpool = Actor("character")
spiderpool_clicked = Actor("character_clicked")

spiderpool.pos = 250, 40
WIDTH = 500
HEIGHT = spiderpool.height + 100


def draw():
    screen.fill((100, 0, 0))
    spiderpool.draw()


def update():
    spiderpool.left = spiderpool.left + 100
    if spiderpool.left > WIDTH:
        spiderpool.right = 0


def reset_spiderpool():
    spiderpool.image = "character"


def on_mouse_down(pos):
    if spiderpool.collidepoint(pos):
        print("Nice!")
        spiderpool.image = "character_clicked"
        clock.schedule_unique(reset_spiderpool, 1.0)

    else:
        print("Do better...")
