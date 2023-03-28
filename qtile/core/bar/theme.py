from importlib import import_module
from libqtile.bar import Bar

from utils import config

themes = [
    'decorated'
]

if config['bar'] in themes:
    module = import_module(f"core.bar.{config['bar']}")
    module.bar.update(
        {'widgets': module.widgets}
    )

    bar: tuple[Bar | None, list] = (
        Bar(**module.bar),
        module.tags,
    )

    simple_module = import_module(f"core.bar.{config['simpleBar']}")
    simple_module.bar.update(
        {'widgets': simple_module.widgets}
    )

    simpleBar: tuple[Bar | None, list] = (
        Bar(**simple_module.bar),
        simple_module.tags,
    )
else:
    bar = (None, [None] * 10)
    simpleBar = (None, [None] * 10)
