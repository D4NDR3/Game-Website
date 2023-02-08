spiderpool = Actor('character')
spiderpool_clicked = Actor('character_clicked')

spiderpool.pos = 250, 40

WIDTH = 500
HEIGHT = spiderpool.height + 100

def draw():
    screen.fill((255,87,51))
    spiderpool.draw()

def update():
        spiderpool.left = spiderpool.left + 5
        if spiderpool.left> WIDTH:
            spiderpool.right = 0

def on_mouse_down(pos):
    if spiderpool.collidepoint(pos):
        print("Nice!")
        spiderpool.image = 'character_clicked'
        clock.schedule_unique(character, 1.0)
    else:
        print("Do better...")




