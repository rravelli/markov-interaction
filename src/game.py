# importing required library
import pygame
from markov import Markov
from graphics.edge import Edge
from graphics.node import Node

from graphics.window import Window

FRICTION = 0.90
MAX_VEL = 70
DELTA_VEL = 1


def open_window(
    layout: dict,
    edges: list[tuple[str, str, dict]],
    node_color: dict[str, pygame.Color] = {},
    node_size: dict[str, int] = {},
    edge_color: dict[tuple[int, int], str] = {},
    markov: Markov = Markov(),
):
    nodes_dict = {
        key: Node(
            pos=layout[key],
            color=node_color.get(key),
            label=key,
            radius=node_size.get(key),
        )
        for key in layout
    }
    edges = [
        Edge(
            nodes_dict[s],
            nodes_dict[e],
            color=edge_color.get((s, e)),
            label=d.get("weight"),
        )
        for s, e, d in edges
    ]

    window = Window(
        layout,
        nodes=list(nodes_dict.values()),
        edges=edges,
        selected_node_label=markov.current_state,
    )
    selected_action = None
    status = True
    dx = 0
    dy = 0
    keys = {}
    while status:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                node = window.on_click(mouse)
                if node:
                    if markov.is_action_state() and node.label in [
                        a.name for a in markov.available_actions()
                    ]:
                        window.selected_node = node.label
                        selected_action = node.label

            elif event.type == pygame.MOUSEWHEEL:
                if event.y < 0:
                    window.zoom_in()
                if event.y > 0:
                    window.zoom_out()

            elif event.type == pygame.KEYDOWN:
                # update key map
                key = event.dict["key"]
                keys[key] = True

                if key == pygame.K_SPACE:
                    if not markov.is_action_state() or selected_action:
                        trans = markov.go_to_next_state(selected_action)
                        selected_action = None
                        if trans is not None:
                            window.selected_node = trans.to

            elif event.type == pygame.KEYUP:
                # update key map
                key = event.dict["key"]
                keys[key] = False

        # iterate over key map
        for key in keys:
            if keys[key]:
                if key == pygame.K_UP:
                    dy = max(dy - DELTA_VEL, -MAX_VEL)
                elif key == pygame.K_DOWN:
                    dy = min(dy + DELTA_VEL, MAX_VEL)
                elif key == pygame.K_LEFT:
                    dx = max(dx - DELTA_VEL, -MAX_VEL)
                elif key == pygame.K_RIGHT:
                    dx = min(dx + DELTA_VEL, MAX_VEL)
        # update dx and dy
        dx *= FRICTION
        dy *= FRICTION
        # translate screen
        window.translate(dx, dy)
        # blanken screen
        window.screen.fill("white")
        # draw everything to the screen
        window.node_history = markov.node_history
        window.action_history = markov.action_history
        window.draw()
        # update the screen
        pygame.display.flip()

    # deactivates the pygame library
    pygame.quit()
