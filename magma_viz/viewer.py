from typing import List

import pygame as pg
import numpy as np

from viztools.drawable.points import Points
from viztools.drawable.lines import Lines
from viztools.drawable.overlay_text import OverlayText
from viztools.viewer import Viewer

from magma_viz.viz_helpers import get_circle_positions

colors = np.random.randint(0, 256, size=(25, 3), dtype=np.uint8)


class MagmaViewer(Viewer):
    def __init__(self, magma: np.ndarray):
        super().__init__(drag_mouse_button=3)
        point_positions = get_circle_positions(magma.shape[0])
        self.points = Points(
            point_positions,
            size=10,
            color=np.array([0, 255, 0, 80])
        )
        self.point_labels = create_point_labels(point_positions)
        self.all_lines: List[List[Lines]] = []
        for i in range(magma.shape[0]):
            row_lines = create_row_lines(magma, i, point_positions)
            self.all_lines.append(row_lines)
        self.show_row_index = 0

    def tick(self, dt: float):
        self.update_drawables([self.points, *self.point_labels])
        # for l in self.all_lines:
        #     self.update_drawables(l)
        self.update_drawables(self.all_lines[self.show_row_index])


    def render(self):
        self.render_coordinate_system()
        self.render_drawables([self.points, *self.point_labels])
        # for l in self.all_lines:
        #     self.render_drawables(l)
        self.render_drawables(self.all_lines[self.show_row_index])

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.show_row_index = (self.show_row_index + 1) % len(self.all_lines)
                self.render_needed = True
            elif event.key == pg.K_DOWN:
                self.show_row_index = (self.show_row_index - 1) % len(self.all_lines)
                self.render_needed = True


def create_point_labels(positions: np.ndarray) -> List[OverlayText]:
    texts = []
    for i, pos in enumerate(positions):
        pos: np.ndarray
        texts.append(OverlayText(f'{i}', pos))
    return texts


def create_row_lines(magma: np.ndarray, row_index: int, point_positions: np.ndarray) -> List[Lines]:
    row = magma[row_index]
    lines = []
    # color = colors[row_index]
    color = np.array([80, 200, 20])
    for i in range(len(magma)):
        pos = point_positions[[i, row[i]]]
        # pos1 = [point_positions[i, 0], 0]
        # pos2 = [point_positions[row[i]][0], 5]
        # pos = np.stack([pos1, pos2], axis=0)
        lines.append(Lines(pos, color=color))
    return lines
