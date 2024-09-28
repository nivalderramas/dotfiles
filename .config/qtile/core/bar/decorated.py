from libqtile import bar
from libqtile.lazy import lazy
# from libqtile.log_utils import logger

from core.bar.utils import base, decoration, iconFont, check_battery_presence, scale_font_size
from extras import GroupBox, modify, TextBox, Volume, widget, Wifi
from libqtile.widget import Clock, Bluetooth
from core.theme import colors

colors_size = len(colors)
icons_fontsize = 18

font_size = scale_font_size(20)


def battery(bg: str, fg: str) -> list:
    """ 
    Check if there is a battery, if not return an empty list, else return the 
    proper widget
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
                fontsize=font_size,
            )]
    else:
        return []


def logo() -> TextBox:
    return modify(
        TextBox,
        **base(colors[0], colors[-1]),
        **decoration(),
        **iconFont(size=int(font_size*1.4)),
        mouse_callbacks={'Button1': lazy.restart()},
        offset=0,
        padding=17,
        text='',
    )


def groups(bg: str, visible) -> GroupBox:
    return GroupBox(
        **iconFont(size=int(font_size*1.6)),
        borderwidth=1,
        block_highlight_text_color=colors[-1],
        visible_groups=visible,
        highlight_method='line',
        highlight_color=[colors[0], colors[0],
                         colors[0], colors[0], colors[-1]],
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
            x=4,
            fontsize=font_size
        ),
        Volume(
            commands={
                'decrease': 'pamixer --decrease 5',
                'increase': 'pamixer --increase 5',
                'get': 'pamixer --get-volume-human',
                'mute': 'pamixer --toggle-mute',
            },
            update_interval=0.1,
            fontsize=font_size,
        ),
    ]


widgets = [
    # LEFT
    widget.Spacer(length=2),
    groups(colors[3], ['1', '2', '3', '4', '5']),

    # CENTER SPACE
    widget.Spacer(),
    logo(),
    widget.Spacer(),

    # RIGHT
    widget.Memory(measure_mem='G', fontsize=font_size),
    widget.Spacer(length=scale_font_size(10)),
    widget.MemoryGraph(type='line', fontsize=font_size),
    widget.Spacer(length=scale_font_size(10)),
    *volume(colors[4], colors[1]),
    widget.Spacer(length=scale_font_size(10)),
    Wifi(format=" {percent:2.0%}", fontsize=font_size,
         mouse_callbacks={
             'Button1': lazy.spawn('networkmanager_dmenu')}),
    # widget.Spacer(
    #     length=scale_font_size_for_4k_monitor(15),
    #     background='#353446',
    # ),

    widget.Spacer(length=scale_font_size(10)),
    Bluetooth(fmt=" {}", hci='/dev_95_05_BB_21_DD_D8', fontsize=font_size),
    widget.Spacer(length=scale_font_size(10)),
    *battery(colors[2], colors[5]),
    widget.Spacer(length=scale_font_size(10)),
    Clock(format='  %d/%m/%y  %H:%M', fontsize=font_size),
    widget.Spacer(length=scale_font_size(10)),
]

widgets_secondary_bar = [
    # LEFT
    widget.Spacer(length=2),
    groups(colors[3], ['8', '9', '0']),

    # CENTER SPACE
    widget.Spacer(),
    logo(),
    widget.Spacer(),

    # RIGHT
    widget.Memory(measure_mem='M'),
    widget.MemoryGraph(type='line'),
    *volume(colors[4], colors[1]),
    Wifi(format=" {percent:2.0%}", width=54, mouse_callbacks={
         'Button1': lazy.spawn('networkmanager_dmenu')}),
    widget.Spacer(
        length=8,
        background='#353446',
    ),

    Bluetooth(fmt=" {}", hci='/dev_95_05_BB_21_DD_D8'),
    *battery(colors[2], colors[5]),
    Clock(format='  %d/%m/%y  %H:%M'),
    widget.Spacer(length=2),
]

bar_config = {
    'background': colors[0],
    'border_color': colors[1],
    'border_width': 4,
    'margin': [5, 5, 5, 5],
    'opacity': 0.9,
    'size': 30,
}


mainBar = bar.Bar(widgets, **bar_config)
secondBar = bar.Bar(widgets_secondary_bar, **bar_config)
