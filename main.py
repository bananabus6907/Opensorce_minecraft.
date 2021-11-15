from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import pygame
import random

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False

punch = Audio('blocks/assets_punch.wav', autoplay=False)

pygame.mixer.init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)
pygame.mixer.music.load('Minecraft.mp3')
pygame.mixer.music.play(-1)



blocks = [
    load_texture('blocks/assets_dia.png'),  # 0
    load_texture('blocks/assets_glass.png'),  # 1
    load_texture('blocks/assets_stone.png'),  # 2
    load_texture('blocks/assets_wood.png'),  # 3
    load_texture('blocks/assets_brick.png'),  # 4
    load_texture('blocks/assets_grass.png'),  # 5
    load_texture('blocks/assets_lava.png'),  # 6
    load_texture('blocks/assets_stonebrick.png'),  # 7
    load_texture('blocks/assets_pumpkin.png'),  # 8
    load_texture('blocks/assets_wool.png'),  # 9
]

block_id = 1


def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]


sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('blocks/assets_sky.jpg'),
    scale=500,
    double_sided=True
)

hand = Entity(
    parent=camera.ui,
    model='block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)


class health:
    health1 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.8, -0.3)
    )

    health2 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.75, -0.3)
    )

    health3 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.7, -0.3)
    )

    health4 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.65, -0.3)
    )

    health5 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.6, -0.3)
    )

    health6 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.55, -0.3)
    )

    health7 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.5, -0.3)
    )

    health8 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.45, -0.3)
    )

    health9 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.4, -0.3)
    )

    health10 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('heart.png'),
        scale=0.05,
        position=Vec2(-0.35, -0.3)
    )


class hunger:
    hunger1 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.8, -0.3)
    )

    hunger2 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.75, -0.3)
    )

    hunger3 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.7, -0.3)
    )

    hunger4 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.65, -0.3)
    )

    hunger5 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.6, -0.3)
    )

    hunger6 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.55, -0.3)
    )

    hunger7 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.5, -0.3)
    )

    hunger8 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.45, -0.3)
    )

    hunger9 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.4, -0.3)
    )

    hunger10 = Entity(
        parent=camera.ui,
        model='cube',
        texture=load_texture('hunger.png'),
        scale=0.05,
        position=Vec2(0.35, -0.3)
    )


def update():
    if held_keys['right mouse'] or held_keys['left mouse']:
        punch.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)


# if held_keys['esc']:
#    stop


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='blocks/assets_grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'left mouse down':
                destroy(self)


class Voxel1(Button):
    def __init__(self, position=(0, 0, 0), texture='blocks/assets_stone.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'left mouse down':
                destroy(self)

class Voxel2(Button):
    def __init__(self, position=(0, 0, 0), texture='blocks/assets_dia.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'left mouse down':
                destroy(self)


for z in range(25):
    for x in range(25):
        voxel = Voxel(position=(x, 0, z))

for z in range(25):
    for x in range(25):
        for y in range(-7, 0, 1):
            voxel1 = Voxel1(position=(x, y, z))

for i in range(25):
    a = random.randrange(1, 21)
    b = random.randrange(-7, 0)
    c = random.randrange(1, 21)
    voxel2 = Voxel2(position=(a, b, c))
player = FirstPersonController()
health()
hunger()
app.run()

