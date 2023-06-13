from core.bar import decorated
from libqtile.log_utils import logger

bar = decorated.mainBar
secondBar = decorated.secondBar

__all__ = [
  'bar',
  'secondBar',
]
