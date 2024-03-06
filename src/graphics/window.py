from __future__ import annotations
import pygame
import graphics.node as _node
import graphics.edge as _edge
import numpy as np
from graphics.colors import *


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
        # pygame.display.set_icon()
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
        margin = 100
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

    def to_draw_scale(self, val: float):
        height = self.screen.get_height()
        width = self.screen.get_width()
        ratio = max(
            width / (self.max_x - self.min_x),
            height / (self.max_y - self.min_y),
        )
        return val * ratio

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
        # height = self.screen.get_height()
        width = self.screen.get_width()
        ratio = (self.max_x - self.min_x) / width
        return val * ratio

    def draw(self):
        for edge in self.edges:
            edge.draw(self, selected=edge.from_node.label == self.selected_node)
        for node in self.nodes:
            node.draw(self, selected=node.label == self.selected_node)
        self.draw_legend()

    def draw_legend(self):
        yellow = False
        for edge in self.edges:
            if edge.from_node.label == self.selected_node and edge.label is None:
                edge.to_node.draw(
                    self,
                    selected=edge.to_node.label == self.selected_node,
                    to_choose=True,
                )
                yellow = True

        if yellow:
            my_font = pygame.font.SysFont("arial", 30)
            text = my_font.render(
                "Choose between yellow actions.",
                True,
                "black",
            )
            text_rect = text.get_rect()
            text_rect.centerx = self.screen.get_width() / 2
            text_rect.centery = self.screen.get_height() - 40
            self.screen.blit(text, text_rect)
        else:
            my_font = pygame.font.SysFont("arial", 30)
            text = my_font.render(
                "Press space bar to go to next state",
                True,
                "black",
            )
            text_rect = text.get_rect()
            text_rect.centerx = self.screen.get_width() / 2
            text_rect.centery = self.screen.get_height() - 40
            self.screen.blit(text, text_rect)

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
