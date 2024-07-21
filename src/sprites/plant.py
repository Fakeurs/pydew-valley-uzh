from src.settings import LAYERS, GROW_SPEED, SCALE_FACTOR
from src.sprites.base import CollideableSprite
from pygame.math import Vector2 as vector


class Plant(CollideableSprite):
    def __init__(self, seed_type, groups, tile, frames):
        super().__init__(tile.rect.center,
                         frames[0], groups, (0, 0), LAYERS['plant'])
        self.rect.center = tile.rect.center + \
            vector(0.5, -3) * SCALE_FACTOR
        self.tile = tile
        self.frames = frames
        self.hitbox = None

        self.seed_type = seed_type
        self.age = 0
        self.max_age = len(self.frames) - 1
        self.grow_speed = GROW_SPEED[seed_type.as_plant_name()]
        self.harvestable = False

    def grow(self):
        if self.tile.watered:
            self.age += self.grow_speed

            if int(self.age) > 0:
                self.z = LAYERS['main']
                self.hitbox = self.rect.inflate(-26, -self.rect.height * 0.4)

            if self.age >= self.max_age:
                self.age = self.max_age
                self.harvestable = True

            self.image = self.frames[int(self.age)]
            self.rect = self.image.get_frect(
                midbottom=self.soil.rect.midbottom + vector(0, 2))
