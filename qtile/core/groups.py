from libqtile.config import Group, Key
from libqtile.lazy import lazy
from typing import Callable
from libqtile.core.manager import Qtile
from libqtile import layout

from core.keys import keys, mod


groups_attr = [
    {"label": "󰈹", "name": "1", },
    {"label": "", "name": "2", },
    {"label": "", "name": "3", },
    {"label": "", "name": "8"},
    {"label": "", "name": "9"},
    {"label": "", "name": "0"},
]
groups = [Group(**g) for g in groups_attr]


def go_to_group(name: str) -> Callable:
    def _inner(qtile: Qtile) -> None:
        if len(qtile.screens) == 1:
            qtile.groups_map[name].cmd_toscreen()
            return

        if name in '123':
            qtile.focus_screen(0)
            qtile.groups_map[name].cmd_toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].cmd_toscreen()

    return _inner


for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))
    keys.append(Key([mod, "shift"],
                    i.name, lazy.window.togroup(i.name),
                    desc="move focused window to group {}".format(i.name)))
