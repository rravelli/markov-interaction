from __future__ import annotations

import graphics.window as window
from graphics.text import TextElement
from pygame import gfxdraw, Color
import numpy as np
from graphics.colors import (
    ACTION_SELECTED_NODE_EDGE,
    DEFAULT_SELECTED_NODE_EDGE,
)


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
        reward: str | float = "",
    ) -> None:
        self.color = color
        self.pos = np.array(pos)
        self.label = str(label) if label else None
        self.radius = radius
        self._r = radius
        self.reward = str(reward) if reward else None

    def draw(
        self,
        window: window.Window,
        selected: bool = False,
        to_choose: bool = False,
    ):
        color = (
            ACTION_SELECTED_NODE_EDGE
            if to_choose
            else (DEFAULT_SELECTED_NODE_EDGE if selected else self.color)
        )

        ratio = 1.5 if selected else 1

        self._r += (self.radius * ratio - self._r) / 10

        draw_pos = window.to_draw_pos(self.pos)
        reward_pos = window.to_draw_pos(self.pos + self._r * 1.5 * np.array([0, -1]))
        radius = window.to_draw_scale(self._r)

        draw_circle(
            window.screen,
            int(draw_pos[0]),
            int(draw_pos[1]),
            int(radius),
            color,
        )
        if self.label:
            TextElement(
                window.screen,
                size=int(window.to_draw_scale(22)),
                color="black",
            ).write(self.label, draw_pos)
        if self.reward:
            TextElement(
                window.screen,
                size=int(window.to_draw_scale(17)),
                color="black",
            ).write(self.reward, reward_pos)

    def inside(self, pos: tuple[float, float], window: window.Window):
        x, y = window.to_draw_pos(self.pos)
        x0, y0 = pos
        return (x - x0) ** 2 + (y - y0) ** 2 <= self.radius * self.radius
