import os
from libqtile import widget
from extras import PowerLineDecoration, RectDecoration

defaults = {
    'font': 'SauceCodePro Nerd Font Medium',
    'fontsize': 20,
    'padding': None,
}


def base(bg: str, fg: str) -> dict:
    return {
        'background': bg,
        'foreground': fg,
    }


def decoration(side: str = '') -> dict:
    return {'decorations': [
        RectDecoration(
            filled=True,
            radius={
                'left': [8, 0, 0, 8],
                'right': [0, 8, 8, 0]
            }.get(side, 8),
            use_widget_background=True,
        )
    ]}


def iconFont(size=30) -> dict:
    return {
        'font': 'SauceCodePro Nerd Font',
        'fontsize': size
    }


def powerline(path: str | list, size=9) -> dict:
    return {'decorations': [
        PowerLineDecoration(
            path=path,
            size=size,
        )
    ]}


def check_battery_presence():
    battery_dirs = [f for f in os.listdir(
        '/sys/class/power_supply') if os.path.isdir(os.path.join('/sys/class/power_supply', f))]
    battery_present = any(f.startswith('BAT') for f in battery_dirs)
    return battery_present


def scale_font_size(font_size):
    """
    Scale the font size for a 4K monitor (27-inch) from the default DPI (1080).

    Args:
        font_size (int): The font size in points.

    Returns:
        int: The scaled font size.
    """
    target_dpi = 75  # DPI for a 4K monitor (27-inch)
    if check_battery_presence():
        target_dpi = 45  # DPI for a normal monitor
    default_dpi = 60

    scale_factor = target_dpi / default_dpi
    scaled_font_size = int(font_size * scale_factor)
    return scaled_font_size
