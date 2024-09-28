from core.groups import groups
from core.keys import keys
from core.layouts import layouts, floating_layout
from core.mouse import mouse
from core.screens import screens
from core.bar.utils import defaults

widget_defaults = defaults.copy()
extension_defaults = defaults.copy()

__all__ = [
  'extension_defaults',
  'keys',
  'floating_layout',
  'groups',
  'layouts',
  'mouse',
  'screens',
  'widget_defaults',
]
