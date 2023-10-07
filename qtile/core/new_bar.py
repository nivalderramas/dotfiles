import os
import socket
from libqtile import widget 
from libqtile.widget.textbox import TextBox


def init_colors():
    return [["#2E3440", "#2E3440"],  # color 0 Background
            ["#37306B", "#37306B"],  # color 1
            ["#66347F", "#66347F"],  # color 2
            ["#9E4784", "#9E4784"],  # color 3
            ["#D27685", "#D27685"],  # color 4
            ["#b172ff", "#b172ff"],  # color 5 - purple-dark
            ["#bf8bff", "#bf8bff"],  # color 6 - ...
            ["#cda5ff", "#cda5ff"],  # color 7 -
            ["#dbbeff", "#dbbeff"],  # color 8 -
            ["#e9d8ff", "#e9d8ff"]]  # color 9 -


colors = init_colors()


def init_layout_theme():
    return {"margin": 50,
            "border_width": 3,
            # "border_focus": "#5e81ac",
            # "border_normal": "#4c566a"
            "border_focus": colors[5],
            "border_normal": colors[9],
            }

# COLORS FOR THE BAR
# Theme name : ArcoLinux Zion
# def init_colors():
#     return [["#4a4a46", "#4a4a46"], # color 0
#             ["#4a4a46", "#4a4a46"], # color 1
#             ["#e3bbf1", "#e3bbf1"], # color 2
#             ["#d33682", "#d33682"], # color 3
#             ["#3384d0", "#3384d0"], # color 4
#             ["#fdf6e3", "#fdf6e3"], # color 5
#             ["#d42121", "#d42121"], # color 6
#             ["#62FF00", "#62FF00"], # color 7
#             ["#9742b5", "#9742b5"], # color 8
#             ["#002b36", "#002b36"]] # color 9

# WIDGETS FOR THE BAR


def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize=22,
                padding=50,
                background=colors[0],
                border_width=0
                )


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e3',
        padding=-13,
        fontsize=140,
        background=bg_color,
        foreground=fg_color)


def upper_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e4',
        padding=-13,
        fontsize=140,
        background=bg_color,
        foreground=fg_color)


def lower_right_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e2',
        padding=-13,
        fontsize=140,
        background=bg_color,
        foreground=fg_color)


def upper_right_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e5',
        padding=-13,
        fontsize=140,
        background=bg_color,
        foreground=fg_color)


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    widgets_list = [
               widget.Spacer(length=30),
               widget.GroupBox(font="FontAwesome",
                               fontsize=22,
                               margin_y=3,
                               margin_x=0,
                               padding_y=6,
                               padding_x=6,
                               borderwidth=0,
                               disable_drag=True,
                               active=colors[5],              # !!! TODO:colors
                               inactive='ffffff',
                               rounded=False,
                               highlight_color=colors[7],
                               highlight_method="line",
                               # this_current_screen_border=colors[0],
                               foreground=colors[0],
                               background=colors[0]
                               ),
               #    widget.Sep(
               #             linewidth=3,
               #             padding=50,
               #             foreground=colors[0],
               #             background=colors[0]
               #             ),
               widget.Spacer(length=20),
               lower_right_triangle(colors[0], colors[5]),
               widget.CurrentLayout(
                        font="Noto Sans",
                        foreground='000000',
                        padding=30,
                        background=colors[5]
                        ),
               upper_left_triangle(colors[0], colors[5]),
               # widget.Sep(
               #          linewidth=3,
               #          padding=50,
               #          foreground=colors[2],
               #          background=colors[1]
               #          ),
               widget.Spacer(length=1060),
               # widget.WindowName(font="Noto Sans",
               #          fontsize=22,
               #          foreground=colors[5],
               #          background=colors[1],
               #          ),
               # widget.Sep(
               #           linewidth=3,
               #           padding=50,
               #           foreground=colors[2],
               #           background=colors[1]
               #           ),
               # widget.Net(
               #          font="Noto Sans",
               #          fontsize=22,
               #          interface="wlo1",
               #          foreground=colors[2],
               #          background=colors[1],
               #          padding=0,
               #          ),
               # widget.Sep(
               #          linewidth=3,
               #          padding=50,
               #          foreground=colors[2],
               #          background=colors[1]
               #          ),
               # widget.NetGraph(
               #          font="Noto Sans",
               #          fontsize=22,
               #          bandwidth="down",
               #          interface="auto",
               #          fill_color=colors[8],
               #          foreground=colors[2],
               #          background=colors[0],
               #          graph_color=colors[8],
               #          border_color=colors[2],
               #          padding=0,
               #          border_width=1,
               #          line_width=1,
               #          ),
               # widget.Sep(
               #          linewidth=3,
               #          padding=50,
               #          foreground=colors[0],
               #          background=colors[0]
               #          ),
               #  # do not activate in Virtualbox - will break qtile
               upper_right_triangle(colors[0], colors[8]),
               widget.ThermalSensor(
                        foreground='000000',
                        foreground_alert=colors[5],
                        background=colors[8],
                        metric=True,
                        padding=30,
                        threshold=80,
                        ),
               # lower_left_triangle(colors[0], colors[8]),# has to be enabled when wanting spaces between widgets
               #  battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
               # widget.Sep(
               #         linewidth=3,
               #         padding=50,
               #         foreground=colors[2],
               #         background=colors[1]
               #         ),
               #  arcobattery.BatteryIcon(
               #           padding=0,
               #           scale=0.7,
               #           y_poss=2,
               #           theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
               #           update_interval=5,
               #           background=colors[1]
               #           ),
               #  # battery option 2  from Qtile
               # widget.Sep(
               #           linewidth=3,
               #           padding=50,
               #           foreground=colors[0],
               #           background=colors[0]
               #           ),
               upper_right_triangle(colors[8], colors[7]),
               widget.Battery(
                       font="Noto Sans",
                       update_interval=10,
                       fontsize=22,
                       foreground='000000',
                       background=colors[7],
                       padding=30
                       ),
               # lower_left_triangle(colors[0], colors[7]),          #has to be enabled when wanting spaces between widgets
               #  widget.Sep(
               #           linewidth=3,
               #           padding=50,
               #           foreground=colors[0],
               #           background=colors[0]
               #           ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[6],
               #          background=colors[1],
               #          padding=0,
               #          fontsize=16
               #          ),
               # widget.CPUGraph(
               #          border_color=colors[2],
               #          fill_color=colors[8],
               #          graph_color=colors[8],
               #          background=colors[1],
               #          border_width=1,
               #          line_width=1,
               #          core="all",
               #          type="box"
               #          ),
               # widget.Sep(
               #          linewidth=3,
               #          padding=50,
               #          foreground=colors[2],
               #          background=colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[4],
               #          background=colors[1],
               #          padding=0,
               #         fontsize=16
               #          ),
               # widget.Memory(
               #          font="Noto Sans",
               #          format='{MemUsed}M/{MemTotal}M',
               #          update_interval=1,
               #          fontsize=12,
               #          foreground=colors[5],
               #          background=colors[1],
               #         ),
               # widget.Sep(
               #          linewidth=3,
               #          padding=50,
               #          foreground=colors[2],
               #          background=colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[3],
               #          background=colors[1],
               #          padding=0,
               #          fontsize=16
               #          ),
               upper_right_triangle(colors[7], colors[6]),
               widget.Clock(
                        foreground='000000',
                        background=colors[6],
                        fontsize=22,
                        format="%Y-%m-%d ... %H:%M",
                        padding=30
                        ),
               # lower_left_triangle(colors[0], colors[6]),          #has to be enabled when wanting spaces between widgets
               # widget.Sep(
               #          linewidth=3,
               #          padding=50,
               #          foreground=colors[5],
               #          background=colors[0]
               #          ),
               upper_right_triangle(colors[6], colors[5]),
               widget.Systray(
                        background=colors[5],
                        icon_size=25,
                        padding=30
                        ),
               lower_left_triangle(colors[0], colors[5]),
               # widget.CheckUpdates(
               #         distro='Arch_checkupdates',
               #         background=colors[1],
               #         foreground=colors[2],
               #         colour_have_updates='ff0000',
               #         colour_no_updates='ffffff',
               #         padding=50,
               #         no_update_string='No updates'
               # ),
               widget.Spacer(length=30),
              ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()
