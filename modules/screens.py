from libqtile import bar
from .widgets import *
from libqtile import widget
from libqtile.config import Screen
from modules.keys import terminal
import os

box_height = 50


def _get_pywal_colors(path):
    out = []
    with open(path) as f:
        for line in f:
            out.append(line.strip())
    return out

colors = _get_pywal_colors('/home/johannes/.cache/wal/colors')

volume = MyVolume(
    fontsize=box_height*0.7,
    font='Font Awesome 5 Free',
    foreground=colors[0],
    background=colors[5],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background=colors[0]),
                # widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background=colors[0]),
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border=colors[9],
                                this_current_screen_border=colors[8],
                                active=colors[7],
                                inactive=colors[2],
                                background=colors[0]),
                widget.TextBox(
                       text = '  ',
                       padding = 0,
                       fontsize = box_height,
                       foreground=colors[0],
                       background=colors[0],
                       ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = box_height,
                       foreground=colors[0],
                       background=colors[0],
                       ),
                # widget.Prompt(),
                # widget.Spacer(length=5),
                widget.WindowName(foreground=colors[7],
                                  background=colors[0],
                                  fmt='{}'),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = box_height,
                       foreground=colors[4],
                       background=colors[0],
                       ),

                widget.CPU(
                    foreground=colors[0],
                  background=colors[4]
                    ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = box_height,
                       foreground=colors[0],
                       background=colors[4],
                       ),
                widget.Memory(
                    measure_mem='G',
                    foreground=colors[4],
                  background=colors[0]
                    ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = box_height,
                       foreground=colors[5],
                       background=colors[0],
                       ),
                volume,
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = box_height,
                       foreground=colors[0],
                       background=colors[5],
                       ),
                widget.Clock(format=' %Y-%m-%d %a %I:%M %p',
                       foreground=colors[7],
                       background=colors[0],),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = box_height,
                       foreground=colors[6],
                       background=colors[0],
                       ),
                widget.BatteryIcon(
                       background=colors[6],),
                widget.Battery(
                       foreground=colors[0],
                       background=colors[6],),
                widget.TextBox(
                    text=' ',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                        },
                   foreground=colors[0],
                   background=colors[6],),
            ],
            box_height,  # height in px
            background=colors[0],
        ),),
]
