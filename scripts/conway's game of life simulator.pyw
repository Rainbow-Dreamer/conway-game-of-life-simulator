import pyglet
from pyglet.window import mouse
import keyboard
import os, sys

abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)
sys.path.append(abs_path)
with open('scripts/settings.py', encoding='utf-8-sig') as f:
    exec(f.read())
window = pyglet.window.Window(*screen_size)
pyglet.resource.path = [abs_path]
for each in ['background_img', 'life_img']:
    each_value = eval(each)
    each_path = os.path.dirname(each_value)
    if each_path:
        if each_path == 'resources':
            exec(f"{each} = '{each_value}'")
        else:
            pyglet.resource.path.append(each_path.replace('/', '\\'))
            exec(f"{each} = '{os.path.basename(each_value)}'")
pyglet.resource.reindex()
image = pyglet.resource.image(background_img)
image.width, image.height = screen_size
block = pyglet.resource.image(life_img)
block.height = block_size
block.width = block_size
mode = 0
rows, columns = screen_size[1] // block_size, screen_size[0] // block_size
whole_places = [[0 for i in range(columns)] for j in range(rows)]
batch = pyglet.graphics.Batch()
whole_lives = [[
    pyglet.sprite.Sprite(block, x=j * block_size, y=i * block_size)
    for j in range(columns)
] for i in range(rows)]
if read_file is not None:
    with open(read_file, encoding='utf-8') as f:
        data = f.read()
    data = data.split('\n')
    M = min(len(data), rows)
    for i in range(M):
        each_line = data[i]
        N = min(columns, len(each_line))
        for j in range(N):
            if each_line[j] != ' ':
                whole_places[rows - i][j] = 1
                whole_lives[rows - i][j].batch = batch


def reset():
    global whole_places
    whole_places = [[0 for i in range(columns)] for j in range(rows)]


def grow():
    global whole_places
    new = [[x for x in y] for y in whole_places]
    for i in range(rows):
        for j in range(columns):
            current_situation = whole_places[i][j]
            neighbour_places = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1),
                                (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1),
                                (i + 1, j + 1)]
            neighbours = [
                whole_places[q[0]][q[1]] for q in neighbour_places
                if 0 <= q[0] < rows and 0 <= q[1] < columns
            ]
            around = neighbours.count(1)
            if current_situation:
                if around not in S:
                    new[i][j] = 0
                    whole_lives[i][j].batch = None
            else:
                if around == B:
                    new[i][j] = 1
                    whole_lives[i][j].batch = batch

    whole_places = new


@window.event
def on_draw():
    global mode
    window.clear()
    image.blit(0, 0)
    batch.draw()
    if mode == 0:
        if keyboard.is_pressed('space'):
            mode = 1
        if keyboard.is_pressed('c'):
            [setattr(v, 'batch', None) for u in whole_lives for v in u]
            reset()
    elif mode == 1:
        pass
        grow()
        if keyboard.is_pressed('q'):
            mode = 0


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button & mouse.LEFT:
        right_x, right_y = x // block_size, y // block_size
        if whole_places[right_y][right_x] == 0:
            whole_places[right_y][right_x] = 1
            whole_lives[right_y][right_x].batch = batch
    elif button & mouse.RIGHT:
        right_x, right_y = x // block_size, y // block_size
        if whole_places[right_y][right_x] == 1:
            whole_places[right_y][right_x] = 0
            whole_lives[right_y][right_x].batch = None


@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    if button & mouse.LEFT:
        right_x, right_y = x // block_size, y // block_size
        try:
            if whole_places[right_y][right_x] == 0:
                whole_places[right_y][right_x] = 1
                whole_lives[right_y][right_x].batch = batch
        except:
            pass
    elif button & mouse.RIGHT:
        right_x, right_y = x // block_size, y // block_size
        try:
            if whole_places[right_y][right_x] == 1:
                whole_places[right_y][right_x] = 0
                whole_lives[right_y][right_x].batch = None
        except:
            pass


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 0.001)
pyglet.app.run()