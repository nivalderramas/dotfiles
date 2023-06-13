from libqtile.config import Screen
from core.bar import bar, secondBar
from libqtile.log_utils import logger

logger.info(bar)
logger.info(secondBar)

screens = [
    Screen(
        wallpaper_mode='fill',
        top=bar,
    ),
    Screen(
        wallpaper_mode='fill',
        top=secondBar,
    ),
    
]
