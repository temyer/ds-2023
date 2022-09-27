from keyword import iskeyword
from typing import Any, Dict

from colorize_mixin import AdvertPrinter, ColorizeMixin


class Advert(ColorizeMixin, AdvertPrinter):
    def __init__(self, mapping: Dict) -> None:
        def unwrap(obj: object, mapping: Dict) -> None:
            for key, item in mapping.items():
                if iskeyword(key):
                    key = key + '_'

                if not isinstance(item, dict):
                    obj.__setattr__(key, item)
                else:
                    obj.__setattr__(key, Advert.__Field())
                    unwrap(obj.__getattribute__(key), item)

        unwrap(self, mapping)

        if not hasattr(self, 'price'):
            self.__setattr__('price', 0)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'price' and __value < 0:
            raise ValueError('must be >= 0')

        super().__setattr__(__name, __value)

    class __Field:
        pass
