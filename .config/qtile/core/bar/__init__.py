from core.bar import decorated
from libqtile.log_utils import logger

mainBar = decorated.mainBar
secondBar = decorated.secondBar

__all__ = [
    'mainBar',
    'secondBar',
]
