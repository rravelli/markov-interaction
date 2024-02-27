import os
from typing import Tuple, Union
from pygame.font import Font
from pygame import Surface
from pygame import draw


class TextElement:
    TEXT_SIZE = 50

    def __init__(
        self,
        surface: Surface,
        size=TEXT_SIZE,
        color="white",
        font_name="Roboto-Regular",
        background=None,
    ) -> None:
        self.surface = surface
        self._font_name = font_name
        self._size = size
        self.color = color
        self.background = background
        self.font = self.__initialize_font()

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        self._font_name = font_name
        self.font = self.__initialize_font()

    @font_name.deleter
    def font_name(self):
        del self._font_name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
        self.font = self.__initialize_font()

    @size.deleter
    def size(self):
        del self._size

    def write(
        self, text: str, coordinates: Union[str, Tuple[int, int]] = "center"
    ):
        rendered_text = self.font.render(text, False, self.color)
        if isinstance(coordinates, str):
            coordinates = self.__calculate_alignment(
                rendered_text, coordinates
            )
        width = rendered_text.get_width()
        height = rendered_text.get_height()
        if self.background:
            draw.rect(
                self.surface,
                self.background,
                (
                    coordinates[0] - width / 2,
                    coordinates[1] - height / 2,
                    width,
                    height,
                ),
            )
        self.surface.blit(
            rendered_text,
            (coordinates[0] - width / 2, coordinates[1] - height / 2),
        )
        return self

    def __calculate_alignment(self, rendered_text, alignment):
        # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect
        # Aligns rendered_text to the surface at the given alignment position
        # e.g: rendered_text.get_rect(center=self.surface.get_rect().center)
        alignment_coordinates = getattr(self.surface.get_rect(), alignment)
        return getattr(rendered_text, "get_rect")(
            **{alignment: alignment_coordinates}
        ).topleft

    def __initialize_font(self):
        return Font(
            os.path.join("assets", "fonts", f"{self._font_name}.ttf"),
            self._size,
        )
