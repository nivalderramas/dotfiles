import os
from libqtile.config import Screen
from core.bar import mainBar, secondBar
from libqtile.log_utils import logger


def check_battery_presence():
    battery_dirs = [f for f in os.listdir(
        '/sys/class/power_supply') if os.path.isdir(os.path.join('/sys/class/power_supply', f))]
    battery_present = any(f.startswith('BAT') for f in battery_dirs)
    return battery_present


def scale_font_size_for_4k_monitor(font_size):
    """
    Scale the font size for a 4K monitor (27-inch) from the default DPI (1080).

    Args:
        font_size (int): The font size in points.

    Returns:
        int: The scaled font size.
    """
    target_dpi = 92  # DPI for a 4K monitor (27-inch)
    if check_battery_presence():
        target_dpi = 45  # DPI for a normal monitor
    default_dpi = 60

    scale_factor = target_dpi / default_dpi
    scaled_font_size = int(font_size * scale_factor)
    return scaled_font_size


screens = [
    Screen(
        wallpaper_mode='fill',
        top=mainBar,
        x=600,
        y=200,
        width=300,
        height=580
    ),
    Screen(
        wallpaper_mode='fill',
        top=secondBar,
    ),

]
