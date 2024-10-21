from libqtile.lazy import lazy
from libqtile.config import Key


scratchpad_name = "scratchpad"
mod = "mod4"
terminal = "kitty"

keys = [
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "brightnessctl set +5%"), desc="less brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "brightnessctl set 5%-"), desc="more brightness"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pamixer --decrease 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pamixer --increase 5")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "Print", lazy.spawn("flameshot gui")),

    Key([mod], "z", lazy.spawn("firefox"), desc="open firefox"),
    Key([mod], "c", lazy.spawn("google-chrome-stable"), desc="open chrome"),
    Key([mod], "t", lazy.spawn("telegram-desktop"), desc="open telegram"),
    Key([mod], "p", lazy.spawn(
        "rofi -show drun"), desc="rofi launch"),
    Key([mod], "e", lazy.spawn(
        "rofimoji"), desc="launch rofimoji"),
    Key([mod], "BackSpace", lazy.spawn(
        "rofi -show window"), desc="rofi window"),
    Key([mod, "shift"], "p", lazy.spawn(
        "rofi -show power-menu -modi power-menu:rofi-power-menu"), desc="rofi"),

    Key([mod], "b", lazy.spawn(
        "rofi-bluetooth"), desc="rofi"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "v", lazy.spawn(
        "pavucontrol"), desc="Open pavucontrol "),
    Key([mod], "v", lazy.spawn('rofi -show rofi-sound -modi rofi-sound:rofi-sound-output-chooser'),
        desc="Rofi pick sound device"),
    Key([mod], "w", lazy.spawn('networkmanager_dmenu'),
        desc="Rofi pick sound device"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # swap
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    # shuffle
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # layout
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

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
    # utils
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "w", lazy.spawn(
        'rofi -show wall -modi "wall:wallpaper-chooser.sh"')),
    Key([mod], "left", lazy.screen.prev_group()),
    Key([mod], "right", lazy.screen.next_group()),
    Key([mod], "Escape", lazy.group[scratchpad_name].hide_all())
]
