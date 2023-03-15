from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import bar, layout, widget
from libqtile.log_utils import logger
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import volume

mod = "mod4"
terminal = "kitty"

fn_keys = [
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="less brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="more brightness"),
    Key([],"XF86AudioLowerVolume",lazy.spawn("amixer sset Master playback 5%-")),
    Key([],"XF86AudioMute"       ,lazy.spawn("amixer -D pulse set Master 1+ toggle")),
    Key([],"XF86AudioRaiseVolume",lazy.spawn("amixer sset Master playback 5%+")),
    Key([],"XF86AudioPlay"       ,lazy.spawn("")),
    Key([],"XF86AudioStop"       ,lazy.spawn("")),
    Key([],"XF86AudioPrev"       ,lazy.spawn("")),
    Key([],"XF86AudioNext"       ,lazy.spawn("")),
]

application_keys = [
    Key([mod], "z", lazy.spawn("firefox"), desc="open firefox"),
    Key([mod], "p", lazy.spawn("rofi -show combi -combi-modes 'window,drun,run'"), desc="rofi"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
]

layout_keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #swap
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    #shuffle
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    #layout
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod,"shift"], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts")
]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    #utils
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]
 

keys.extend(fn_keys)
keys.extend(application_keys)
keys.extend(layout_keys)
