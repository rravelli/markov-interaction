from __future__ import annotations

import graphics.window as window
from graphics.node import Node
from graphics.text import TextElement
import pygame
from math import sqrt
import numpy as np

ARROW_WIDTH = 10
ARROW_LENGTH = 20


class Edge:
    def __init__(
        self,
        from_node: Node,
        to_node: Node,
        color: str = "white",
        label: str | float = None,
        width: int = 4,
    ) -> None:
        self.color = color
        self.from_node = from_node
        self.to_node = to_node
        self.label = str(label) if label else None
        self.width = width if label else 10

    def draw(self, window: window.Window, selected: bool = False):
        self.draw_line(window=window, selected=selected)
        self.draw_arrow(window=window, selected=selected)
        self.draw_label(window=window)

    def draw_line(self, window: window.Window, selected: bool):
        if self.from_node == self.to_node:
            return

        start_pos = self.from_node.pos
        end_pos = self.to_node.pos
        color = "green" if selected else self.color

        vec: np.ndarray = end_pos - start_pos
        vec /= np.linalg.norm(vec)

        margin = window.to_real_scale(
            self.to_node.radius + ARROW_LENGTH - self.width
        )
        pygame.draw.line(
            window.screen,
            color,
            window.to_draw_pos(start_pos),
            window.to_draw_pos(end_pos - margin * vec),
            self.width,
        )

    def draw_label(self, window: window.Window):
        if self.label:
            x1, y1 = self.from_node.pos
            x2, y2 = self.to_node.pos
            pos = window.to_draw_pos(((x1 + x2) / 2, (y1 + y2) / 2))
            TextElement(window.screen, size=22).write(self.label, pos)

    def draw_arrow(self, window: window.Window, selected: bool):
        color = "green" if selected else self.color
        start_pos = self.from_node.pos
        end_pos = self.to_node.pos
        vec: np.ndarray = end_pos - start_pos
        vec /= np.linalg.norm(vec)

        arrow_point = end_pos - window.to_real_scale(self.to_node.radius) * vec
        arrow_center = arrow_point - window.to_real_scale(ARROW_LENGTH) * vec

        vert_vec_x = 1 / sqrt(1 + (vec[0] / vec[1]) ** 2)
        vert_vec_y = 1 / sqrt(1 + (vec[1] / vec[0]) ** 2)
        vert_vec = np.array([vert_vec_x, vert_vec_y])

        arrow_width = window.to_real_scale(self.width + ARROW_WIDTH)
        arrow_up = arrow_center + arrow_width / 2 * vert_vec
        arrow_down = arrow_center - arrow_width / 2 * vert_vec
        pygame.draw.polygon(
            window.screen,
            color,
            [
                window.to_draw_pos(arrow_point),
                window.to_draw_pos(arrow_up),
                window.to_draw_pos(
                    arrow_center + window.to_real_scale(4) * vec
                ),
                window.to_draw_pos(arrow_down),
            ],
        )
