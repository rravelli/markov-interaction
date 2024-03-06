from __future__ import annotations

import graphics.window as window
from graphics.node import Node
from graphics.text import TextElement
import pygame
from math import sqrt
import numpy as np
from graphics.colors import (
    ACTION_SELECTED_NODE_EDGE,
    DEFAULT_SELECTED_NODE_EDGE,
)

ARROW_WIDTH = 10
ARROW_LENGTH = 20
LOOP_RADIUS = 25


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
        self.offset = 10 * np.random.random(2)

    def draw(self, window: window.Window, selected: bool = False):
        self.draw_line(window=window, selected=selected)
        self.draw_arrow(window=window, selected=selected)
        self.draw_label(window=window, selected=selected)

    def draw_line(self, window: window.Window, selected: bool):
        color = (
            (
                ACTION_SELECTED_NODE_EDGE
                if self.label is None
                else DEFAULT_SELECTED_NODE_EDGE
            )
            if selected
            else self.color
        )

        if self.from_node == self.to_node:
            center = self.from_node.pos - (
                LOOP_RADIUS + self.from_node._r / 2
            ) * np.array([1, 0])
            delta = LOOP_RADIUS * np.array([1, 1])
            pos = window.to_draw_pos(center - delta)
            size = window.to_draw_scale(2 * LOOP_RADIUS)
            rect = (pos[0], pos[1], size, size)
            pygame.draw.arc(
                window.screen,
                color,
                rect,
                (-20 + 90) / 57,
                (270 + 90) / 57,
                1,
            )
            return

        start_pos = self.from_node.pos
        end_pos = self.to_node.pos

        vec: np.ndarray = end_pos - start_pos
        vec /= np.linalg.norm(vec)

        margin = self.to_node._r + ARROW_LENGTH - self.width
        pygame.draw.aaline(
            window.screen,
            color,
            window.to_draw_pos(start_pos),
            window.to_draw_pos(end_pos - margin * vec),
            # self.width,
        )

    def draw_label(self, window: window.Window, selected: bool):
        if self.label is None:
            return

        if self.from_node == self.to_node:
            pos = self.from_node.pos - (
                2 * LOOP_RADIUS + self.from_node._r / 2
            ) * np.array([1, 0])
        else:
            pos = (
                self.from_node.pos + self.to_node.pos
            ) / 2 + self.parallel_vec() * 15

        pos = window.to_draw_pos(pos)
        TextElement(
            window.screen,
            size=int(window.to_draw_scale(20)),
            color=DEFAULT_SELECTED_NODE_EDGE if selected else "black",
            background="white" if self.from_node == self.to_node else None,
        ).write(self.label, pos)

    def parallel_vec(self):
        start_pos = self.from_node.pos
        end_pos = self.to_node.pos
        vec: np.ndarray = end_pos - start_pos
        vec /= np.linalg.norm(vec)
        if vec[1] == 0:
            vert_vec_x = 0
            vert_vec_y = 1
        else:
            if start_pos[0] > end_pos[0]:
                factor = 1
            else:
                factor = -1
            vert_vec_x = factor / sqrt(1 + (vec[0] / vec[1]) ** 2)
            vert_vec_y = -vec[0] * vert_vec_x / vec[1]

        return np.array([vert_vec_x, vert_vec_y])

    def draw_arrow(self, window: window.Window, selected: bool):
        if self.from_node == self.to_node:
            start_pos = self.to_node.pos - np.array([2, 1.5])
            end_pos = self.to_node.pos - np.array([0, 0])
        else:
            start_pos = self.from_node.pos
            end_pos = self.to_node.pos

        color = (
            (
                ACTION_SELECTED_NODE_EDGE
                if self.label is None
                else DEFAULT_SELECTED_NODE_EDGE
            )
            if selected
            else self.color
        )

        vec: np.ndarray = end_pos - start_pos
        vec /= np.linalg.norm(vec)

        arrow_point = end_pos - self.to_node._r * vec
        arrow_center = arrow_point - ARROW_LENGTH * vec

        if vec[1] == 0:
            vert_vec_x = 0
            vert_vec_y = 1
        else:
            vert_vec_x = 1 / sqrt(1 + (vec[0] / vec[1]) ** 2)
            vert_vec_y = -vec[0] * vert_vec_x / vec[1]

        vert_vec = np.array([vert_vec_x, vert_vec_y])

        arrow_up = arrow_center + ARROW_WIDTH / 2 * vert_vec
        arrow_down = arrow_center - ARROW_WIDTH / 2 * vert_vec

        points = [
            window.to_draw_pos(arrow_point),
            window.to_draw_pos(arrow_up),
            window.to_draw_pos(arrow_center + 4 * vec),
            window.to_draw_pos(arrow_down),
        ]

        pygame.draw.polygon(window.screen, color, points)
        pygame.draw.polygon(
            window.screen, pygame.Color(0, 0, 0), points, width=1
        )
