class AdvertPrinter:
    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:
    repr_color_code = 33

    def __repr__(self) -> str:
        content = super().__repr__()

        return '\033[0;{};40m{}\033[0m'.format(
            self.repr_color_code,
            content
        )
