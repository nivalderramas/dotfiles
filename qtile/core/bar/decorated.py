import os
from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.bar.utils import base, decoration, iconFont, powerline
from extras import Battery, GroupBox, modify, TextBox, Volume, widget, Wifi
from libqtile.widget import Clock, Bluetooth
from utils import color


tags = [
    '󰈹', '', ''
]

bar = {
    'background': color['bg'],
    'border_color': color['bg'],
    'border_width': 4,
    'margin': [5, 5, 5, 5],
    'opacity': 1,
    'size': 30,
}

def check_battery_presence():
    battery_dirs = [f for f in os.listdir('/sys/class/power_supply') if os.path.isdir(os.path.join('/sys/class/power_supply', f))]
    battery_present = any(f.startswith('BAT') for f in battery_dirs)
    return battery_present

def battery(bg: str, fg: str) -> list:
    """ 
    Check if there is a battery, if not return an empty list, else return the proper widget
    """
    # Example usage
    if check_battery_presence():
        return [
            widget.BatteryIcon(
                 theme_path='~/.config/qtile/assets/Battery/',
                 background=bg,
                 scale=1,
            ),
            widget.Battery(
                font='JetBrains Mono Bold',
                background=bg,
                foreground=fg,
                format='{percent:2.0%}',
                fontsize=13,
            )]
    else:
        return []


def sep(fg: str, offset=0, padding=8) -> TextBox:
    return TextBox(
        **base(None, fg),
        **iconFont(),
        offset=offset,
        padding=padding,
        text='}',
    )


def logo(bg: str, fg: str) -> TextBox:
    return modify(
        TextBox,
        **base(bg, fg),
        **decoration(),
        **iconFont(),
        mouse_callbacks={'Button1': lazy.restart()},
        offset=0,
        padding=17,
        text='',
    )


def groups(bg: str) -> GroupBox:
    return GroupBox(
        **iconFont(),
        background=bg,
        borderwidth=1,
        colors=[
            color['fg'], color['fg'], color['fg'],
        ],
        highlight_color=bg,
        block_highlight_text_color=[color['blue']],
        visible_groups=['1', '2', '3'],
        highlight_method='line',
        inactive=color['black'],
        invert=True,
        padding=12,
        rainbow=True,
    )


def volume(bg: str, fg: str) -> list:
    return [
        TextBox(
            text='',
            x=4
        ),
        Volume(
            commands={
                'decrease': 'pamixer --decrease 5',
                'increase': 'pamixer --increase 5',
                'get': 'pamixer --get-volume-human',
                'mute': 'pamixer --toggle-mute',
            },
            update_interval=0.1,
        ),
    ]


def window_name(bg: str, fg: str) -> object:
    return widget.WindowName(
        **base(bg, fg),
        **iconFont(25),
        format='{name}',
        max_chars=60,
        width=CALCULATED,
    )


def cpu(bg: str, fg: str) -> list:
    return [
        modify(
            TextBox,
            **base(bg, fg),
            **decoration('left'),
            **iconFont(),
            offset=3,
            text='',
            x=5,
        ),
        widget.CPU(
            **base(bg, fg),
            **powerline('arrow_right'),
            format='{load_percent:.0f}%',
        )
    ]


def ram(bg: str, fg: str) -> list:
    return [
        TextBox(
            **base(bg, fg),
            **iconFont(),
            offset=-2,
            padding=5,
            text='﬙',
            x=-2,
        ),
        widget.Memory(
            **base(bg, fg),
            **powerline('arrow_right'),
            format='{MemUsed: .0f}{mm} ',
            padding=-1,
        ),
    ]


def disk(bg: str, fg: str) -> list:
    return [
        TextBox(
            **base(bg, fg),
            **iconFont(),
            offset=-1,
            text='',
            x=-5,
        ),
        widget.DF(
            **base(bg, fg),
            **powerline('arrow_right'),
            format='{f} GB  ',
            padding=0,
            partition='/',
            visible_on_warn=False,
            warn_color=fg,
        ),
    ]


def clock(bg: str, fg: str) -> list:
    return [
        modify(
            TextBox,
            **base(bg, fg),
            **decoration('left'),
            **iconFont(),
            offset=2,
            text='',
            x=4,
        ),
        modify(
            Clock,
            **base(bg, fg),
            **decoration('right'),
            format='%A - %I:%M %p ',
            long_format='%B %-d, %Y ',
            padding=6,
        ),
    ]


widgets = [
    #LEFT
    widget.Spacer(length=2),
    groups(color['bg']),
    widget.Notify(),

    #CENTER SPACE
    widget.Spacer(),
    logo(color['bg'], color['fg']),
    widget.Spacer(),

    #RIGHT
    *volume(color['bg'],color['fg']),
    Wifi(format=" {percent:2.0%}",width=54, mouse_callbacks={'Button1': lazy.spawn('networkmanager_dmenu')}),
    widget.Spacer(
                    length=8,
                    background='#353446',
                ),

    Bluetooth(fmt=" {}", hci='/dev_95_05_BB_21_DD_D8'),
    *battery(color['bg'],color['fg']),
    widget.Clock(format='  %d/%m/%y  %H:%M'),
    widget.Spacer(length=2),
]
