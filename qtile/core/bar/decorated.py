import os
from libqtile import bar
from libqtile.lazy import lazy
from libqtile.log_utils import logger

from core.bar.utils import base, decoration, iconFont, powerline
from extras import Battery, GroupBox, modify, TextBox, Volume, widget, Wifi
from libqtile.widget import Clock, Bluetooth
from core.theme import colors

colors_size = len(colors)



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



def logo() -> TextBox:
    return modify(
        TextBox,
        **base(colors[0], colors[-1]),
        **decoration(),
        **iconFont(),
        mouse_callbacks={'Button1': lazy.restart()},
        offset=0,
        padding=17,
        text='',
    )


def groups(bg: str, visible) -> GroupBox:
    return GroupBox(
        **iconFont(),
        borderwidth=1,
        block_highlight_text_color=colors[-1],
        visible_groups=visible,
        highlight_method='line',
        highlight_color=[colors[0],colors[0],colors[0],colors[0],colors[-1]],
        inactive=colors[1],
        active=colors[-2],
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


widgets = [
    #LEFT
    widget.Spacer(length=2),
    groups(colors[3],['1','2','3']),
    widget.Notify(),

    #CENTER SPACE
    widget.Spacer(),
    logo(),
    widget.Spacer(),

    #RIGHT
    widget.Memory(measure_mem='M'),
    widget.MemoryGraph(type='line'),
    *volume(colors[4],colors[1]),
    Wifi(format=" {percent:2.0%}",width=54, mouse_callbacks={'Button1': lazy.spawn('networkmanager_dmenu')}),
    widget.Spacer(
                    length=8,
                    background='#353446',
                ),

    Bluetooth(fmt=" {}", hci='/dev_95_05_BB_21_DD_D8'),
    *battery(colors[2],colors[5]),
    Clock(format='  %d/%m/%y  %H:%M'),
    widget.Spacer(length=2),
]

widgets_secondary_bar = [
    #LEFT
    widget.Spacer(length=2),
    groups(colors[3],['8','9','0']),
    widget.Notify(),

    #CENTER SPACE
    widget.Spacer(),
    logo(),
    widget.Spacer(),

    #RIGHT
    widget.Memory(measure_mem='M'),
    widget.MemoryGraph(type='line'),
    *volume(colors[4],colors[1]),
    Wifi(format=" {percent:2.0%}",width=54, mouse_callbacks={'Button1': lazy.spawn('networkmanager_dmenu')}),
    widget.Spacer(
                    length=8,
                    background='#353446',
                ),

    Bluetooth(fmt=" {}", hci='/dev_95_05_BB_21_DD_D8'),
    *battery(colors[2],colors[5]),
    Clock(format='  %d/%m/%y  %H:%M'),
    widget.Spacer(length=2),
]

bar_config = {
    'background': colors[0],
    'border_color': colors[1],
    'border_width': 4,
    'margin': [5, 5, 5, 5],
    'opacity': 1,
    'size': 30,
}

tags = [
    '󰈹', '', ''
]

mainBar = bar.Bar(widgets,**bar_config)
secondBar = bar.Bar(widgets_secondary_bar,**bar_config)
