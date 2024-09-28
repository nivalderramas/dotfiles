from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from typing import Callable
from libqtile.core.manager import Qtile

from core.keys import keys, mod


groups_attr = [
    {"label": "󰈹", "name": "1"},
    {"label": "", "name": "2"},
    {"label": "󰞷", "name": "3"},
    {"label": "", "name": "4"},
    {"label": "", "name": "5"},
    {"label": "", "name": "8"},
    {"label": "", "name": "9"},
    {"label": "", "name": "0"},
]

groups = [Group(**g) for g in groups_attr]


def go_to_group(name: str) -> Callable:
    def _inner(qtile: Qtile) -> None:
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '12345':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner


for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))
    keys.append(Key([mod, "shift"],
                    i.name, lazy.window.togroup(i.name),
                    desc="move focused window to group {}".format(i.name)))

# Configure Scratchpad

scratchpad_name = "scratchpad"
python_dropdown = "python"
kitty_dropdown = "kitty"
telegram_dropdown = "telegram"
qtile_debugger_dropdown = "qtile_debugger"


logs_path = "/home/nivalderramas/.local/share/qtile/qtile.log"
logs_cmd = "kitty --hold tail -f {logs_path}"

scratchpad_items = [
    {
        "item": DropDown(
            kitty_dropdown,
            "kitty"
        ),
        "trigger": Key(["control"], "1", lazy.group[scratchpad_name].dropdown_toggle(kitty_dropdown))
    },
    {
        "item": DropDown(
            python_dropdown,
            "kitty python"
        ),
        "trigger": Key(["control"], "2", lazy.group[scratchpad_name].dropdown_toggle(python_dropdown))
    },
    {
        "item": DropDown(
            telegram_dropdown,
            "telegram-desktop"
        ),
        "trigger": Key(["control"], "3", lazy.group[scratchpad_name].dropdown_toggle(telegram_dropdown))
    },
]

groups.append(
    ScratchPad(scratchpad_name, [d["item"] for d in scratchpad_items])
)

keys.extend([d["trigger"] for d in scratchpad_items])
