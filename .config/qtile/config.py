# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from core import (
    screens,
    keys,
    mouse,
    groups,
)
import os
import subprocess
import re
from libqtile import layout, qtile
from libqtile.config import Match
from libqtile import hook
from core.theme import colors
from libqtile.log_utils import logger


log_level = "INFO"
systemErrorTitle = "SYSTEM ERROR"
systemInfoTitle = "SYSTEM INFO"


def sendNotification(title, msj):
    subprocess.run(["notify-send", title, msj])


valid_log_levels = [
    'CRITICAL',
    'FATAL',
    'ERROR',
    'WARN',
    'WARNING',
    'INFO',
    'DEBUG',
    'NOTSET'
]


logger.setLevel(log_level)
sendNotification(systemInfoTitle, f"Log level: {log_level}")


# This must be loeaded so variables are available

mod = "mod4"
terminal = "kitty"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([home])


config = {
    'border_focus': colors[4],
    'border_normal': "#afafaa",
    'border_width': 4,
    'margin': 10,
    'single_border_width': 4,
    'single_margin': 10,
}

layouts = [
    layout.MonadTall(**config),
    layout.Max(),
    layout.VerticalTile(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
cursor_warp = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
