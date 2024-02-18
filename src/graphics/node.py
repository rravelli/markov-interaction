from __future__ import annotations

import graphics.window as window
from graphics.text import TextElement
import pygame
from pygame import gfxdraw, Color
import numpy as np


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


class Node:

    def __init__(
        self,
        pos: tuple[float, float],
        color: Color = Color(255, 255, 255),
        radius: int = 20,
        label: str | float = "",
    ) -> None:
        self.color = color
        self.pos = np.array(pos)
        self.label = str(label) if label else None
        self.radius = radius
        self._r = radius

    def draw(self, window: window.Window, selected: bool = False):
        ratio = 1.3 if selected else 1

        self._r += (self.radius * ratio - self._r) / 20

        draw_pos = window.to_draw_pos(self.pos)

        draw_circle(
            window.screen,
            int(draw_pos[0]),
            int(draw_pos[1]),
            int(self._r),
            pygame.Color(0, 255, 0) if selected else self.color,
        )
        if self.label:
            TextElement(window.screen, size=22).write(self.label, draw_pos)

    def inside(self, pos: tuple[float, float], window: window.Window):
        x, y = window.to_draw_pos(self.pos)
        x0, y0 = pos
        return (x - x0) ** 2 + (y - y0) ** 2 <= self.radius * self.radius