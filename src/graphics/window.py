from __future__ import annotations
import pygame
import graphics.node as _node
import graphics.edge as _edge
import numpy as np


class Window:
    def __init__(
        self,
        node_pos: dict[str, tuple[float, float]],
        nodes: list[_node.Node] = [],
        edges: list[_edge.Edge] = [],
        selected_node_label: str = None,
    ) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 700), pygame.RESIZABLE)
        # set the pygame window name
        pygame.display.set_caption("Markov")
        self._rescale(list(node_pos.values()))
        self.nodes = nodes
        self.edges = edges
        self.selected_node = selected_node_label

    def _rescale(self, coordinates: list[tuple[float, float]]):
        self.min_x = float("inf")
        self.max_x = float("-inf")
        self.min_y = float("inf")
        self.max_y = float("-inf")
        for pos in coordinates:
            x, y = pos
            if x < self.min_x:
                self.min_x = x
            if x > self.max_x:
                self.max_x = x
            if y < self.min_y:
                self.min_y = y
            if y > self.max_y:
                self.max_y = y
        margin = 0.1
        self.min_x -= margin
        self.max_x += margin
        self.min_y -= margin
        self.max_y += margin

    def to_draw_pos(self, pos: tuple[float, float]):
        x, y = pos
        height = self.screen.get_height()
        width = self.screen.get_width()
        return np.array(
            [
                (x - self.min_x) * width / (self.max_x - self.min_x),
                (y - self.min_y) * height / (self.max_y - self.min_y),
            ]
        )

    def to_real_pos(self, pos: tuple[float, float]):
        x, y = pos
        height = self.screen.get_height()
        width = self.screen.get_width()
        return np.array(
            [
                self.min_x + x * (self.max_x - self.min_x) / width,
                self.min_y + y * (self.max_y - self.min_y) / height,
            ]
        )

    def to_real_scale(self, val: float):
        height = self.screen.get_height()
        width = self.screen.get_width()
        ratio = max(
            (self.max_x - self.min_x) / width,
            (self.max_y - self.min_y) / height,
        )
        return val * ratio

    def draw(self):
        for edge in self.edges:
            edge.draw(
                self, selected=edge.from_node.label == self.selected_node
            )
        for node in self.nodes:
            node.draw(self, selected=node.label == self.selected_node)

    def on_click(self, pos: tuple[float, float]) -> _node.Node:
        for node in self.nodes:
            if node.inside(pos, self):
                return node

    def translate(self, dx: int, dy: int):
        self.min_x += dx
        self.max_x += dx
        self.min_y += dy
        self.max_y += dy

    def zoom_in(self, factor=100):
        dx = (self.max_x - self.min_x) / factor
        dy = (self.max_y - self.min_y) / factor
        self.min_x += dx
        self.max_x -= dx
        self.max_y -= dy
        self.min_y += dy

    def zoom_out(self, factor=100):
        dx = (self.max_x - self.min_x) / factor
        dy = (self.max_y - self.min_y) / factor
        self.min_x -= dx
        self.max_x += dx
        self.max_y += dy
        self.min_y -= dy
