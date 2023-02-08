spiderpool = Actor('character')
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

